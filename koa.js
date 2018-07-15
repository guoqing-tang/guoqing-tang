
const Koa = require('koa');


const mykoa = new Koa();

// 对于任何请求，app将调用该异步函数处理请求：
mykoa.use(async (tgq, next) => {
    await next();
    tgq.response.type = 'text/html';
    tgq.response.body = '<h1>Hello, koa2!</h1>';
});

// 在端口8080监听:
tgq.listen(8080);
console.log('Server running at http://localhost:8080/');