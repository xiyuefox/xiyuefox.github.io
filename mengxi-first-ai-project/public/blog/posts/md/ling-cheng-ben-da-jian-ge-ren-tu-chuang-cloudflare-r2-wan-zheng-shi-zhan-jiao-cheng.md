---
title: "零成本搭建个人图床：Cloudflare R2完整实战教程"
date: 2026-03-17
tags: [tech, tutorial]
category: "obsidian"
badge: "tech"
type: "article"
---

# 🎉 零成本搭建个人图床！Cloudflare R2 完整实战教程

> 适合人群：博主、开发者、公众号运营者
> 关键词：免费图床 | Cloudflare R2 | 永久存储 | 全球 CDN

---
![image](https://xixi-image-bed.jinxiyue07.workers.dev/1764908366629-no52e.png)
## 💡 为什么选择 Cloudflare R2？

传统图床的痛点：
- ❌ 免费额度用完就收费
- ❌ 访问速度慢，经常失效
- ❌ 有水印或广告
- ❌ 隐私安全无保障

**Cloudflare R2 的优势：**
- ✅ **10GB 永久免费存储**
- ✅ **通过 Workers 访问零流量费**
- ✅ **全球 CDN 加速，访问飞快**
- ✅ **完全掌控，数据安全**
- ✅ **无限次上传/下载（免费额度内）**

---

## 🚀 搭建步骤（5步完成）

### **第一步：注册 Cloudflare 账号**

1. 访问 [Cloudflare Dashboard](https://dash.cloudflare.com/sign-up)
2. 注册并验证邮箱
3. 登录到控制台

> 💡 提示：无需信用卡，完全免费

---

### **第二步：创建 R2 存储桶**

```
1. 左侧菜单选择「R2」
2. 点击「Create bucket」
3. 输入存储桶名称（如：my-image-bed）
4. 选择区域：Asia Pacific（亚太）
5. 点击「Create bucket」
```

✅ 存储桶创建成功！

---

### **第三步：创建 Worker**

```
1. 左侧菜单选择「Workers 和 Pages」
2. 点击「创建应用程序」
3. 选择「创建 Worker」
4. 输入名称（如：image-upload）
5. 点击「部署」
```

---

### **第四步：编辑 Worker 代码**

部署后点击「编辑代码」，删除默认代码，粘贴以下代码：

```javascript
export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    // 检查 R2 绑定
    if (!env.MY_BUCKET) {
      return new Response(JSON.stringify({
        success: false,
        error: 'R2 bucket not configured'
      }), {
        status: 500,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' }
      });
    }

    // 上传接口
    if (request.method === 'POST' && url.pathname === '/upload') {
      try {
        const formData = await request.formData();
        const file = formData.get('file');

        if (!file) {
          return new Response(JSON.stringify({
            success: false,
            error: '没有上传文件'
          }), {
            status: 400,
            headers: { ...corsHeaders, 'Content-Type': 'application/json' }
          });
        }

        // 生成文件名
        const timestamp = Date.now();
        const randomStr = Math.random().toString(36).substring(2, 8);
        const extension = file.name.split('.').pop() || 'jpg';
        const fileName = `${timestamp}-${randomStr}.${extension}`;

        // 上传到 R2
        await env.MY_BUCKET.put(fileName, file.stream(), {
          httpMetadata: {
            contentType: file.type || 'image/jpeg',
          },
        });

        const imageUrl = `${url.origin}/${fileName}`;

        return new Response(JSON.stringify({
          success: true,
          url: imageUrl,
          filename: fileName
        }), {
          headers: {
            ...corsHeaders,
            'Content-Type': 'application/json',
          },
        });
      } catch (error) {
        return new Response(JSON.stringify({
          success: false,
          error: error.message
        }), {
          status: 500,
          headers: { ...corsHeaders, 'Content-Type': 'application/json' }
        });
      }
    }

    // 获取图片
    if (request.method === 'GET') {
      const key = url.pathname.slice(1);

      if (!key) {
        return new Response('图床 API 运行中 ✅', {
          headers: corsHeaders,
        });
      }

      const object = await env.MY_BUCKET.get(key);

      if (!object) {
        return new Response('Image not found', {
          status: 404,
          headers: corsHeaders,
        });
      }

      const headers = new Headers();
      object.writeHttpMetadata(headers);
      headers.set('Cache-Control', 'public, max-age=31536000');
      Object.entries(corsHeaders).forEach(([k, v]) => {
        headers.set(k, v);
      });

      return new Response(object.body, { headers });
    }

    return new Response('Method not allowed', {
      status: 405,
      headers: corsHeaders,
    });
  },
};
```

点击「保存并部署」

---

### **第五步：绑定 R2 存储桶**

这是**最关键**的一步！

```
1. 在 Worker 页面，点击「设置」→「绑定」
2. 点击「添加绑定」
3. 填写：
   - 绑定类型：R2 bucket
   - 变量名称：MY_BUCKET（必须完全一致！）
   - R2 存储桶：选择你创建的存储桶
4. 点击「保存」
5. 重新部署 Worker
```

⚠️ **注意**：变量名必须是 `MY_BUCKET`，与代码中的 `env.MY_BUCKET` 对应！

---

## 🎨 创建上传页面

创建一个 `upload.html` 文件：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>图床上传</title>
    <style>
        body {
            font-family: -apple-system, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        #drop-zone {
            border: 3px dashed #ddd;
            border-radius: 15px;
            padding: 60px 20px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s;
        }
        #drop-zone:hover {
            border-color: #667eea;
            background: #f0f4ff;
        }
        .drop-icon {
            font-size: 64px;
            margin-bottom: 20px;
        }
        #result {
            margin-top: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 10px;
            display: none;
        }
        .url-input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-family: monospace;
            margin: 10px 0;
        }
        .copy-btn {
            padding: 8px 20px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        #preview {
            max-width: 100%;
            margin-top: 20px;
            border-radius: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📸 图床上传</h1>

        <div id="drop-zone">
            <div class="drop-icon">📤</div>
            <div>点击或拖拽图片到这里上传</div>
            <input type="file" id="file-input" accept="image/*" style="display:none">
        </div>

        <div id="result">
            <h3 style="color: #28a745;">✅ 上传成功！</h3>
            <label><strong>图片链接：</strong></label>
            <input type="text" id="image-url" class="url-input" readonly>
            <button class="copy-btn" onclick="copyUrl()">复制链接</button>

            <label style="display: block; margin-top: 15px;"><strong>Markdown：</strong></label>
            <input type="text" id="markdown-url" class="url-input" readonly>
            <button class="copy-btn" onclick="copyMarkdown()">复制 Markdown</button>

            <img id="preview" src="" alt="预览">
        </div>
    </div>

    <script>
        // 替换为你的 Worker 地址
        const UPLOAD_API = 'https://your-worker.workers.dev/upload';

        const dropZone = document.getElementById('drop-zone');
        const fileInput = document.getElementById('file-input');
        const result = document.getElementById('result');
        const imageUrl = document.getElementById('image-url');
        const markdownUrl = document.getElementById('markdown-url');
        const preview = document.getElementById('preview');

        dropZone.addEventListener('click', () => fileInput.click());

        dropZone.addEventListener('dragover', (e) => {
            e.preventDefault();
            dropZone.style.borderColor = '#667eea';
        });

        dropZone.addEventListener('drop', (e) => {
            e.preventDefault();
            const files = e.dataTransfer.files;
            if (files.length > 0) uploadFile(files[0]);
        });

        fileInput.addEventListener('change', (e) => {
            if (e.target.files.length > 0) uploadFile(e.target.files[0]);
        });

        async function uploadFile(file) {
            const formData = new FormData();
            formData.append('file', file);

            try {
                dropZone.innerHTML = '<div class="drop-icon">⏳</div><div>上传中...</div>';

                const response = await fetch(UPLOAD_API, {
                    method: 'POST',
                    body: formData
                });

                const data = await response.json();

                if (data.success) {
                    imageUrl.value = data.url;
                    markdownUrl.value = `![image](${data.url})`;
                    preview.src = data.url;
                    result.style.display = 'block';
                    dropZone.innerHTML = '<div class="drop-icon">✅</div><div>上传成功！继续上传？</div>';
                } else {
                    alert('上传失败：' + data.error);
                    dropZone.innerHTML = '<div class="drop-icon">📤</div><div>点击或拖拽图片到这里上传</div>';
                }
            } catch (error) {
                alert('上传失败：' + error.message);
                dropZone.innerHTML = '<div class="drop-icon">📤</div><div>点击或拖拽图片到这里上传</div>';
            }
        }

        function copyUrl() {
            imageUrl.select();
            document.execCommand('copy');
            alert('✅ 链接已复制！');
        }

        function copyMarkdown() {
            markdownUrl.select();
            document.execCommand('copy');
            alert('✅ Markdown 已复制！');
        }
    </script>
</body>
</html>
```

⚠️ 记得修改 `UPLOAD_API` 为你的 Worker 地址！

---

## 🧪 测试验证

### **1. 测试 Worker 是否运行**
访问：`https://your-worker.workers.dev`
应该看到：`图床 API 运行中 ✅`

### **2. 测试上传功能**
- 用浏览器打开 `upload.html`
- 拖拽或点击上传图片
- 成功后会显示图片 URL 和 Markdown 格式

### **3. 测试图片访问**
复制上传后的 URL，在浏览器中打开，应该能看到图片

---

## 🔥 常见问题排查

### **问题1：500 错误**
```
错误：Internal server error: R2 bucket not configured
```
**解决方案：**
- 检查 Worker 的「绑定」标签页
- 确认变量名是 `MY_BUCKET`（区分大小写）
- 确认已选择正确的 R2 存储桶
- 重新部署 Worker

### **问题2：上传失败**
**检查清单：**
- [ ] Worker 代码是否正确部署
- [ ] R2 绑定是否配置
- [ ] 上传页面的 API 地址是否正确
- [ ] 查看 Worker 日志（Dashboard → Worker → 日志）

### **问题3：图片无法访问**
**可能原因：**
- Worker 路由配置问题
- R2 存储桶权限问题
- 文件名或路径错误

---

## 🎯 进阶优化

### **1. 绑定自定义域名**
```
Worker 设置 → 触发器 → 自定义域
添加：img.yourdomain.com
```

### **2. 添加文件大小限制**
在代码中添加：
```javascript
if (file.size > 5 * 1024 * 1024) {
  return new Response(JSON.stringify({
    success: false,
    error: '文件不能超过 5MB'
  }), { status: 400 });
}
```

### **3. 限制文件类型**
```javascript
const allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];
if (!allowedTypes.includes(file.type)) {
  return new Response(JSON.stringify({
    success: false,
    error: '只允许上传图片'
  }), { status: 400 });
}
```

---

## 📊 成本分析

| 项目 | 免费额度 | 超出费用 |
|:---|:---|:---|
| **存储空间** | 10 GB | $0.015/GB/月 |
| **A 类操作**（上传） | 100万次/月 | $4.50/百万次 |
| **B 类操作**（下载） | 1000万次/月 | $0.36/百万次 |
| **Worker 请求** | 10万次/天 | 免费 |

💡 **结论**：个人使用基本不会超出免费额度！

---

## ✨ 最终效果

- ✅ 上传速度快，访问稳定
- ✅ 支持拖拽上传、自动生成 Markdown
- ✅ 全球 CDN 加速，访问飞快
- ✅ 完美适配 Obsidian、Notion、公众号等

---

## 💬 写在最后

Cloudflare R2 图床适合：
- 📝 博主：写作配图
- 👨‍💻 开发者：项目文档
- 📱 公众号运营：文章插图
- 🎓 学生：笔记管理

**零成本、稳定可靠，再也不用担心图片失效或限速了！**

---

**觉得有用？点赞+在看，让更多人看到！** 🌟

我是纯纯小白小溪！之前折腾公众号配图+发文章，半天时间耗在「找图床→传图→调格式」的死

循环里…

直到遇到Claude Code！它像个耐心的技术搭子✨：

- 手把手教我配置Cloudflare R2图床，一步错都不行的那种！

- 还能自动生成Obsidian笔记存教程，再也不用手抄步骤～

- 图床搞定后直接一键发公众号，效率从「半天熬秃头」缩到「1小时搞定摸鱼去」！

原来用对工具，「麻烦的小事」真的能变「一键快乐」！

毕竟啊——这个时代，把时间省下来摸鱼、冥想、养生、少花钱多攒钱，才是真正的「生命意义」

～









