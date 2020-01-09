# Extract-words-from-pictures

## 功能

识别图片中的文字并将结果存放于剪贴板

针对某文库或者其他不让复制文字等情况，可识别已有图片或剪贴板中的图片

## 环境

基于 ```https://github.com/wwtm/gitpython_examples/tree/master/20200102-实时截图识别OCR``` 改进

适用于macOS系统，Windows系统使用若报encoding方面的错则需要在文件读写处加入 ```encoding = 'utf-8'```

Python 版本 ： python3

## 使用方法

初次使用，需要安装依赖库
```
pip3 install package-name
```
或
```
pip install package-name
```
package-name包括 ```pillow```, ```baidu-aip``` 和 ```pyperclip```

安装完成后，使用截图工具将需要识别的区域截图到剪贴板，然后运行程序，识别结果将自动输出在屏幕上，同时保存在剪贴板中，直接在需要的地方ctrl+v粘贴即可，不需要手动复制输出的结果

## 注意事项

1、若需要识别已有文件，则需按程序中的说明注释掉部分语句，并修改文件名，直接截图到剪贴板更加方便高效

2、程序默认识别到行末自动换行，如不需要换行（即识别整段文字）则需注释掉程序第31行，并取消注释第32行

3、程序默认会将输出文件删除，如需要将结果存放在文件中，请注释掉程序第40行，结果文件将存放在与此程序相同的目录中

4、若出现下面这中错误，说明截图失败，只需重新截图即可
```
AttributeError: 'NoneType' object has no attribute 'save'
```

## 百度智能云账号

此程序需要百度智能云账号，粗略识别每天免费50000次，精确识别每天免费500次

注册网址 ```https://login.bce.baidu.com/?account=```

注册完成后创建应用即可。

