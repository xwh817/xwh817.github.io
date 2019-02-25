### ButterKnife
1. 强大的View绑定和Click事件处理功能，简化代码，提升开发效率
2. 方便的处理Adapter里的ViewHolder绑定问题
3. 运行时不会影响APP效率，使用配置方便
4. 代码清晰，可读性强

- **介绍**  
主要是解决掉findViewById和setOnXXListener，还包括资源的注入，IOC，运行时注解（上次）和编译时注解（ButterKnife注解）。

- **ButterKnife原理**  
主要采用编译时注解，说白了就是用apt生成代码

- **GitHub**  
https://github.com/JakeWharton/butterknife

### 绑定上下文
```java
    /**
    * 在Activity中绑定：
    * 在setContentView之后绑定，不用手动解绑。
    */
    @Override  
    protected void onCreate(Bundle savedInstanceState) {  
        super.onCreate(savedInstanceState);  
        setContentView(R.layout.activity_main);  
        // 在setContentView之后绑定
        ButterKnife.bind(this);  
    }
    
    /**
    * 在Fragment中绑定：
    * 必须在onDestroyView()中做解绑操作。
    */
    @Override  
    public View onCreateView(LayoutInflater inflater, ViewGroup container,  
                             Bundle savedInstanceState) {  
        View view = inflater.inflate(R.layout.fragment, container, false);  
        //返回一个Unbinder值（进行解绑），注意这里的this指当前fragment
        unbinder = ButterKnife.bind(this, view);  
        return view;  
    }
    
    /**
    * 在Adapter的ViewHolder中绑定：
    */
    class ViewHolder {  
    @BindView(R.id.title) TextView name;  
    @BindView(R.id.job) TextView job;  

    public ViewHolder(View view) {  
      ButterKnife.bind(this, view);  
    }  
  }  

```


### 资源绑定（注入）
```java
    // 绑定View
    @BindView( R2.id.button)  
    private Button button;   
    
    // 绑定多个View
    @BindViews({ R2.id.button1, R2.id.button2,  R2.id.button3})  
    private List<Button> buttonList ;
    
    //绑定资源文件中string字符串  
    @BindString(R2.string.app_name)  
    private String str; 
    
    //绑定string里面array数组  
    @BindArray(R2.array.city)
    String [] citys ;
    
    //绑定图片资源  
    @BindBitmap( R2.mipmap.bm)
    public Bitmap bitmap ;
    
    //绑定颜色值 
    @BindColor( R2.color.colorAccent )  
    int black ;  
    
```


### 事件绑定
```java
    // 给 button1设置一个点击事件
    @OnClick(R2.id.button1 )
    public void showToast(){  
        Toast.makeText(this, "is a click", Toast.LENGTH_SHORT).show();  
    }
    
    //长按事件
    @OnLongClick(R2.id.button1)
    
    // 多个View的绑定(多条点击事件是没有用R2的方式，如果一定要使用R2的写法，可以单一逐次写)
    @OnClick({R.id.bt1, R.id.bt2})

```