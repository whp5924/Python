
目录
   
   浏览器抓包
   =
        打开google chrome浏览器按 F12 或 在页面元素上右键点击,选择‘检查'
    
            1. Elements（元素面板）：使用“元素”面板可以通过自由操纵DOM和CSS来重演您网站的布局和设计。

            2. Console（控制台面板）：在开发期间，可以使用控制台面板记录诊断信息，或者使用它作为 shell，
                在页面上与JavaScript交互

            3. Sources（源代码面板）：在源代码面板中设置断点来调试 JavaScript ，或者通过Workspaces（工作区）
                连接本地文件来使用开发者工具的实时编辑器

            4. Network（网络面板）：从发起网页页面请求Request后得到的各个请求资源信息（包括状态、资源类型、大小、
                所用时间等），并可以根据这个进行网络性能优化

            5. Performance（性能面板）：使用时间轴面板，可以通过记录和查看网站生命周期内发生的各种事件来提高
                页面运行时的性能

            6. Memory（内存面板）：分析web应用或者页面的执行时间以及内存使用情况

            7. Application（应用面板）：记录网站加载的所有资源信息，包括存储数据（Local Storage、Session Storage、
                -IndexedDB、Web SQL、Cookies）、缓存数据、字体、图片、脚本、样式表等

            8. Security（安全面板）：使用安全面板调试混合内容问题，证书问题等等

            9. Audits（审核面板）：对当前网页进行网络利用情况、网页性能方面的诊断，并给出一些优化建议。
                 比如列出所有没有用到的CSS文件等
        
   如图：
   = 
 <div align=center>
	
  <img width = "500" height = "200" src="https://raw.githubusercontent.com/whp5924/sample/master/.README_images/2d353110.png" alt="来了">   
  
 </div>
                     
        *网络面板*
               
            
             1. 第一排:             Controls控件*  

             2. 第二排 第三排：     Filter 过滤器
                
             3. 第四排:             Overview 概览
                
             4. 第五排:             Request Table 请求列表
                
             5. 底部:               Summary 概要
   
 <img width="400" height="200" align=cenger src="https://raw.githubusercontent.com/whp5924/sample/master/.README_images/controls.png" alt="过滤器说明">
 
 </br>:  
    
        第一、Controls控制 如上图所示
        第二、Filter 过滤器
            
            使用这些选项可以控制在 请求列表 中显示哪些资源.
            ** 提示**: 按住 Ctrl,然后点击过滤器可以同时选择多个过滤器.
            筛选框可以实现很多定制化的筛选，如:字符串匹配、关键词筛选.
            
                domain: 显示来自指定域的资源，可以使用通配符()来包括多个域。
                    如：.com 显示以.com结尾的所有域名中的资源. DevTools 会在自动完成下拉菜单
                        中自动填充它遇到的所有域.
    
                has-response-header：显示包含指定HTTP响应头信息的资源。 
                    DevTools会在自动完成下拉菜单中自动填充它遇到的所有响应头。

                is：通过is:running找出WebSocket请求。

                larger-than(大于)：显示大于指定大小的资源（以字节为单位）。设置值1000等效于设置值1k。

                method(方法)：显示通过指定的HTTP方法类型检索的资源。DevTools使用它遇到的所有HTTP方法填充下拉列表。

                mime-type（mime类型：显示指定MIME类型的资源。 DevTools使用它遇到的所有MIME类型填充下拉列表。

                mixed-content（混合内容：显示所有混合内容资源（mixed-content:all）或仅显示当前显示的内容
                    （mixed-content:displayed）。

                Scheme（协议）：显示通过不受保护的HTTP（scheme:http）或受保护的HTTPS（scheme:https）检索的资源。

                set-cookie-domain（cookie域）：显示具有Set-Cookie头,并且其Domain属性与指定值匹配的资源。
                    DevTools会在自动完成下拉菜单中自动填充它遇到的所有Cookie域。

                set-cookie-name（cookie名）：显示具有Set-Cookie头,并且名称与指定值匹配的资源。
                    DevTools会在自动完成下拉菜单中自动填充它遇到的所有Cookie名。

                set-cookie-value（cookie值）：显示具有Set-Cookie头,并且值与指定值匹配的资源。
                    DevTools会在自动完成下拉菜单中自动填充它遇到的所有cookie值。

                status-code（状态码）：仅显示其HTTP状态代码与指定代码匹配的资源。
                    DevTools会在自动完成下拉菜单中自动填充它遇到的所有状态码。

        第三、Overview（概览）

            这个图表显示检索资源的时间轴。如果您看到多个垂直堆叠的栏，这意味着这些资源被同时检索。
        
        第四、Requests Table（请求列表）

            此列表列出了检索的每个资源。默认情况下，此表按时间顺序排序，也就是最早的资源在顶部。
            单击资源名称可以获得更多信息。提示：右键单击列表的任何标题栏可以以添加或删除信息列。

            查看单个资源的详细信息

                点击资源名称（位于 Requests Table 的 Name 列下）可以查看与该资源有关的更多信息。 

                可用标签会因您所选择资源类型的不同而不同，但下面四个标签最常见：

                Headers：与资源关联的 HTTP 标头。

                Preview：JSON、图像和文本资源的预览。

                Response：HTTP 响应数据（如果存在）。

                Timing：资源请求生命周期的精细分解。

                Headers（查看 HTTP 标头）  
                   
            点击 Headers 可以显示该资源的标头。
                
                Headers 标签可以显示资源的请求网址、HTTP 方法以及响应状态代码。 
                该标签还会列出 HTTP 响应和请求标头、它们的值以及任何查询字符串参数  
                
 <img width="400" height="200" src="https://raw.githubusercontent.com/whp5924/sample/master/.README_images/header.png" alt="header说明">
 
   </br>:
            
            点击每一部分旁边的 view source 或 view parsed 链接，您能够以源格式或者解析格式查看响应标头、
            请求标头或者查询字符串参数。
 <img width="400" height="200" src="https://raw.githubusercontent.com/whp5924/sample/master/.README_images/response.png">           
            
            点击Preview标签可以查看该资源的预览。Preview标签可能显示一些有用的信息，
            也可能不显示，具体取决于您所选择资源的类型
    
        Response(查看http响应内容)
            点击 Response 标签可以查看资源未格式化的 HTTP 响应内容。 Preview 标签可能包含一些有用的信息，
            也可能不包含，具体取决于您所选择资源的类型.
 <img width="400" height="200" src="https://raw.githubusercontent.com/whp5924/sample/master/.README_images/response1.png">
        
        Cookie
            点击 Cookies 标签可以查看在资源的 HTTP 请求和响应标头中传输的 Cookie 表。 只有传输 Cookie 时，此标签才可用。

            下面是 Cookie 表中每一列的说明：

                Name：Cookie 的名称。

                Value：Cookie 的值。

                Domain：Cookie 所属的域。

                Path：Cookie 来源的网址路径。

                Expires / Max-Age：Cookie 的 expires 或 max-age 属性的值。

                Size：Cookie 的大小（以字节为单位）。

                HTTP：指示 Cookie 应仅由浏览器在 HTTP 请求中设置，而无法通过 JavaScript 访问。

                Secure：如果存在此属性，则指示 Cookie 应仅通过安全连接传输。

                复制、保存和清除网络信息

            
            右键单击Requests Table（请求列表）以复制、保存或删除网络信息。一些选项是上下文相关的，所以如果想在单个资源上操作，需要右键单击该资源行。下面的列表描述了每个选项

                Copy Response（复制响应）

                    将所选资源的HTTP响应复制到系统剪贴板。

                Copy as cURL（复制为cURL）

                    将所选资源的网络请求作为cURL命令字符串复制到系统剪贴板。 请参阅将复制请求为cURL命令。

                    curl命令是一个利用URL规则在命令行下工作的文件传输工具。它支持文件的上传和下载，所以是综合传输工具，但按传统，习惯称curl为下载工具。作为一款强力工具，curl支持包括HTTP、HTTPS、ftp等众多协议，还支持POST、cookies、认证、从指定偏移处下载部分文件、用户代理字符串、限速、文件大小、进度条等特征。做网页处理流程和数据检索自动化，curl可以祝一臂之力。l

                Copy All as HAR（全部复制为HAR）

                    将所有资源复制到系统剪贴板作为HAR数据。 HAR文件包含描述网络“瀑布”的JSON数据结构。一些第三方工具可以使用HAR文件中的数据重建网络瀑布。有关详细信息，请参阅Web性能强大工具：HTTP归档（HAR）。

                Save as HAR with Content（另存为带内容的HAR）

                    将所有网络数据与每个页面资源一起保存到HAR文件中。 二进制资源（包括图像）被编码为Base64编码文本。

                Clear Browser Cache（清除浏览器缓存）

                    清除浏览器高速缓存。提示：您也可以从Network Conditions(网络条件)抽屉式窗格中启用或禁用浏览器缓存。

                Clear Browser Cookies（清除浏览器Cookie）

                    清除浏览器的Cookie。

                Open in Sources Panel（在源文件面板中打开）

                    在Sources(源文件)面板中打开选定的资源。

                Open Link in New Tab（在新标签页中打开链接）

                    在新标签页中打开所选资源。您还可以在Requests Table(请求列表)中双击资源名称。

                Copy Link Address（复制链接地址）

                    将资源URL复制到系统剪贴板。

                Save（保存）

                    保存所选的文本资源。仅显示在文本资源上。

                Replay XHR（重新发送XHR）

                    重新发送所选的XMLHTTPRequest。仅显示在XHR资源上。

                查看资源发起者和依赖关系

                按住Shift并移动鼠标到资源上可查看它的发起者和依赖关系。这部分是你鼠标悬停的资源的target(目标)引用。

                从target(目标)往上查找，第一个颜色编码为绿色的资源是target(目标)的发起者。如果存在第二个颜色编码
                为绿色资源，那么这个是发起者的发起者。从target(目标)向下查找，任何颜色编码为红色的资源都是target的依赖。


               
        
        
        
        
    
    
    标题
    文本
        普通文本
        单行文本
        多行文本
        文字高亮
        换行
        斜体
        粗体
        删除线
    图片
        来源于网络的图片
        GitHub仓库中的图片
    链接
        文字超链接
            链接外部URL
            链接本仓库里的URL
        锚点
        图片链接
    列表
        无序列表
        有序列表
        复选框列表
    块引用
    代码高亮
    表格
    表情
    diff语法

横线
  
  
*___可以显示横线效*
标题
    一级标题
                            二级标题
三级标题
四级标题
五级标题
六级标题
文本
普通文本

这是一段普通的文本
单行文本

Hello,大家好，我是果冻虾仁。

在一行开头加入1个Tab或者4个空格。
文本块
语法1

在连续几行的文本开头加入1个Tab或者4个空格。

'''欢迎到访'''
很高兴见到您
**祝您，早上好，中午好，下午好，晚安**

语法2

使用一对各三个的反引号：

*欢迎到访*





我是C++码农

你可以在知乎、

CSDN、简书搜索  

【果冻虾仁】找到我

该语法也可以实现代码高亮，见代码高亮
文字高亮

文字高亮功能能使行内部分文字高亮，使用一对反引号。 语法：

`linux` `网络编程` `socket` `epoll` 

效果：linux 网络编程 socket epoll

也适合做一篇文章的tag
换行

直接回车不能换行，
可以在上一行文本后面补两个空格，
这样下一行的文本就换行了。

或者就是在两行文本直接加一个空行。

也能实现换行效果，不过这个行间距有点大。
斜体、粗体、删除线
语法 	效果
*斜体1* 	*斜体1*
_斜体2_ 	斜体2
**粗体1** 	粗体1
__粗体2__ 	粗体2
这是一个 ~~删除线~~ 	这是一个 删除线
***斜粗体1*** 	斜粗体1
___斜粗体2___ 	斜粗体2
***~~斜粗体删除线1~~*** 	斜粗体删除线1
~~***斜粗体删除线2***~~ 	斜粗体删除线2

  ***斜体、粗体、删除线可混合使用***

图片

基本格式：

![alt](URL title)

alt和title即对应HTML中的alt和title属性（都可省略）：

    alt表示图片显示失败时的替换文本
    title表示鼠标悬停在图片时的显示文本（注意这里要加引号）

URL即图片的url地址，如果引用本仓库中的图片，直接使用相对路径就可了，如果引用其他github仓库中的图片要注意格式，即：仓库地址/raw/分支名/图片路径，如：

https://github.com/guodongxiaren/ImageCache/raw/master/Logo/foryou.gif

# 	语法 	效果
1 	![baidu](http://www.baidu.com/img/bdlogo.gif "百度logo") 	baidu
2 	![][code-past] 	

注意例2的写法使用了URL标识符的形式，在链接一节有介绍。

    在文末有code-past的定义：

[code-past]:https://img-blog.csdnimg.cn/201908060004034.png

链接
链接外部URL
# 	语法 	效果
1 	[我的博客](http://blog.csdn.net/guodongxiaren "悬停显示") 	我的博客
2 	[我的知乎][zhihu] 	我的知乎

语法2由两部分组成：

    第一部分使用两个中括号，[ ]里的标识符（本例中zhihu），可以是数字，字母等的组合，标识符上下对应就行了（姑且称之为URL标识符）
    第二部分标记实际URL。

    使用URL标识符能达到复用的目的，一般把全文所有的URL标识符统一放在文章末尾，这样看起来比较干净。

        URL标识符是我起的名字，不知道是否准确。囧。。

链接本仓库里的URL
语法 	效果
[我的简介](/example/profile.md) 	[我的简介]
[example](./example) 	example
图片链接

给图片加链接的本质是混合图片显示语法和普通的链接语法。普通的链接中[ ]内部是链接要显示的文本，而图片链接[ ]里面则是要显示的图片。
直接混合两种语法当然可以，但是十分啰嗦，为此我们可以使用URL标识符的形式。
# 	语法 	效果
1 	[![weibo-logo]](http://weibo.com/linpiaochen) 	weibo-logo
2 	[![](/img/zhihu.png "我的知乎，欢迎关注")][zhihu] 	
3 	[![csdn-logo]][csdn] 	csdn-logo

因为图片本身和链接本身都支持URL标识符的形式，所以图片链接也可以很简洁（见例3）。
注意，此时鼠标悬停时显示的文字是图片的title，而非链接本身的title了。

    本文URL标识符都放置于文末

锚点

其实呢，每一个标题都是一个锚点，和HTML的锚点（#）类似，比如我们
语法 	效果
    [回到顶部](#readme) 	回到顶部

不过要注意，标题中的英文字母都被转化为小写字母了。

    以前GitHub对中文支持的不好，所以中文标题不能正确识别为锚点，但是现在已经没问题啦！

列表
无序列表
语法

* 昵称：果冻虾仁
- 别名：隔壁老王
* 英文名：Jelly

效果

    昵称：果冻虾仁

    别名：隔壁老王

    英文名：Jelly

多级无序列表
语法

* 编程语言
    * 脚本语言
        * Python

效果

    编程语言
        脚本语言
            Python

一级有序列表
语法

就是在数字后面加一个点，再加一个空格。不过看起来起来可能不够明显。

面向对象的三个基本特征：

1. 封装
2. 继承
3. 多态

效果

面向对象的三个基本特征：

    封装
    继承
    多态

多级有序列表

和无序列表一样，有序列表也有多级结构。
语法

1. 这是一级的有序列表，数字1还是1
   1. 这是二级的有序列表，阿拉伯数字在显示的时候变成了罗马数字
      1. 这是三级的有序列表，数字在显示的时候变成了英文字母

效果

    这是一级的有序列表，数字1还是1
        这是二级的有序列表，阿拉伯数字在显示的时候变成了罗马数字
            这是三级的有序列表，数字在显示的时候变成了英文字母

复选框列表
语法

- [x] 需求分析
- [x] 系统设计
- [x] 详细设计
- [x] 编码
- [ ] 测试
- [ ] 交付

效果

    需求分析
    系统设计
    详细设计
    编码
    测试
    交付

您可以使用这个功能来标注某个项目各项任务的完成情况。

    Tip:

        在GitHub的issue中使用该语法是可以实时点击复选框来勾选或解除勾选的，而无需修改issue原文。

块引用
常用于引用文本
文本摘自《深入理解计算机系统》P27

　令人吃惊的是，在哪种字节顺序是合适的这个问题上，人们表现得非常情绪化。实际上术语“little endian”（小端）和“big endian”（大端）出自Jonathan Swift的《格利佛游记》一书，其中交战的两个派别无法就应该从哪一端打开一个半熟的鸡蛋达成一致。因此，争论沦为关于社会政治的争论。只要选择了一种规则并且始终如一的坚持，其实对于哪种字节排序的选择都是任意的。

    “端”（endian）的起源
    以下是Jonathan Swift在1726年关于大小端之争历史的描述：
    “……下面我要告诉你的是，Lilliput和Blefuscu这两大强国在过去36个月里一直在苦战。战争开始是由于以下的原因：我们大家都认为，吃鸡蛋前，原始的方法是打破鸡蛋较大的一端，可是当今的皇帝的祖父小时候吃鸡蛋，一次按古法打鸡蛋时碰巧将一个手指弄破了，因此他的父亲，当时的皇帝，就下了一道敕令，命令全体臣民吃鸡蛋时打破较小的一端，违令者重罚。”

块引用有多级结构
语法

> 数据结构
>> 树
>>> 二叉树
>>>> 平衡二叉树
>>>>> 满二叉树

效果

    数据结构

        树

            二叉树

                平衡二叉树

                    满二叉树

代码高亮
语法

在三个反引号后面加上编程语言的名字，另起一行开始写代码，最后一行再加上三个反引号。
效果

public static void main(String[]args){} //Java

int main(int argc, char *argv[]) //C

echo "hello GitHub" #Bash

document.getElementById("myH1").innerHTML="Welcome to my Homepage"; //javascipt

string &operator+(const string& A,const string& B) //cpp

${PROJECT_NAME} - 当前的项目名  
${NAME} - 在文件创建过程中，新文件对话框的命名  
${USER} - 当前的登录用户  
${DATE} - 现在的系统日期  
${TIME} - 现在的系统时间  
${YEAR} - 当前年份  
${MONTH} - 当前月份  
${DAY} - 当前月份中的第几日  
${HOUR} - 现在的小时  
${MINUTE} - 现在的分钟  
${PRODUCT_NAME} - IDE创建文件的名称  
${MONTH_NAME_SHORT} - 月份的前三个字母缩写  
${MONTH_NAME_FULL} - 完整的月份名

