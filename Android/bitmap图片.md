
- **图片用法**
```java
// imageView加载本地文件图片
imageView.setImageURI(Uri.fromFile(new File(filePath)));

```


- **Bitmap占用内存大小**
> 一个BitMap位图占用的内存 = 长度 * 宽度 * 单位像素占用的字节数。  
Bitmap bitmap = Bitmap.createBitmap(1024, 1024, Bitmap.Config.ARGB_8888);
该bitmap占用4Mb的空间  1K * 1K * 4bt

>Bitmap 的内存申请不同版本间有些许差异，在 3.0-7.0 的 bitmap 像素内存都是存放在 Java heap 中的，而 8.0 以后则是放在 Native heap 中的  
https://www.jianshu.com/p/8e8ad414237e

- **从相机获取Bitmap**
```java
protected Bitmap getBitmapFromCamera() {
		Bitmap bmp = null;
		try {
			YuvImage image = new YuvImage(getTempData(), ImageFormat.NV21, mCameraSize.width, mCameraSize.height, null);
			if (image != null) {
				ByteArrayOutputStream stream = new ByteArrayOutputStream();
				// 经测试quality设成其他值貌似没啥用，图片大小基本没变（原因：这儿只影响保存为图片文件时的大小，Bitmap占内存大小只和像素点多少有关）
				image.compressToJpeg(new Rect(0, 0, mCameraSize.width, mCameraSize.height), 100, stream);
				bmp = BitmapFactory.decodeByteArray(stream.toByteArray(), 0, stream.size());
				stream.close();

				bmp = BitmapUtils.rotateBitmap(bmp, 90);        // 相机默认90度角

                // 按照选取框比例切图，保证得到的是选取框内的图
				Rect rect = ScanUtil.getRect(mContext);
				bmp = BitmapUtils.cropBitmap(bmp, rect);  
				// 缩放成需要的尺寸
				bmp = BitmapUtils.scaleBitmap(bmp, 260f / bmp.getWidth());

			}
		} catch (Exception ex) {
			ex.printStackTrace();
		}

		return bmp;
	}
```

- **压缩Bitmap，保存为JPG、PNG**
```java
/**
* CompressFormat: 图片格式, Bitmap.CompressFormat.JPEG/PNG
* quality：0~100，图片质量，越小占内存越小，越模糊。
*/
public static boolean saveBitmapToLocal(Bitmap bitmap, File file_img, CompressFormat format, int quality) {
		try {
			file_img.createNewFile();
			OutputStream outStream = new FileOutputStream(file_img);
			bitmap.compress(format, quality, outStream);
			outStream.flush();
			outStream.close();
			return true;
		} catch (Exception e) {
			e.printStackTrace();
		}

		return false;
	}
```


- Bitmap Options
- [参数列表](https://www.cnblogs.com/nimorl/p/8065071.html)
- [参考](https://blog.csdn.net/showdy/article/details/54378637)