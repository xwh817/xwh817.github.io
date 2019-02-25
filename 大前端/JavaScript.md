## 语法
- 从一个对象里面截取变量或函数，类似import {} from
```javascript
const { navigation } = this.props;  // 从一个对象中取属性
let {navigate} = this.props.navigation; // 后面的代码就可以直接使用navigate()函数了。
```