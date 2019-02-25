### newInstant问题，为什么不用new
- fragment是通过反射进行重建的（例如切换横竖屏时），而且只调用了无参构造的方法。
- 查看源代码，fragment在初始化之后，f.setArguments(args); 会把参数保存在arguments中，当再次重建onCreate()时可以拿到之前设置的参数。
- fragment在重建的时候不会调用有参构造，通过new Fragment()时，设置的参数就没有了，可能出现空指针异常！