import tornado.ioloop
import tornado.web

class mainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" 
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head> 
<title> New Document </title>
<meta name="Generator" content="EditPlus">
<meta name="Author" content="">
<meta name="Keywords" content=""> 
<meta name="Description" content=""> 
</head>
<body>
<h1>九九乘法表</h1>
<script type="text/javascript">
for(var i=1;i<=9;i++){
    for(var j=1;j<=i;j++){
        document.write(j+"*"+i+"="+i*j+"&nbsp;&nbsp;&nbsp;&nbsp;");
    }
    document.write('<br/>');
}
</script>
</body>

</html>

''')
class ptHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" 
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head> 
<title> New Document </title>
<meta name="Generator" content="EditPlus">
<meta name="Author" content="">
<meta name="Keywords" content=""> 
<meta name="Description" content=""> 
</head>
<body>
<h1>九九乘法表</h1>
<script type="text/javascript">
for(var i=1;i<=4;i++){
    for(var j=1;j<=i;j++){
        document.write(j+"*"+i+"="+i*j+"&nbsp;&nbsp;&nbsp;&nbsp;");
    }
    document.write('<br/>');
}
</script>
</body>

</html>

''')

application = tornado.web.Application([
    (r"/", mainHandler),
    (r"/4", ptHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
