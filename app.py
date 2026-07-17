from flask import Flask, render_template_string

app = Flask(__name__)

blocks = [
    {
        "title": "Хрустальное сердце",
        "text": "изделия из хрустальных бусин",
        "images": ["https://sun9-37.userapi.com/s/v1/ig2/BTFtngld_8esSaCb-i9uDI-HrwRT9hX9qNsdkvb1hOL0HHgHEVYrsXzhsp65pgpPn7CIJVCzDSGjjwtKX0k1Sc0K.jpg?quality=95&as=32x57,48x85,72x128,108x192,160x285,240x427,360x640,480x854,540x961,640x1139,720x1281,1080x1921,1280x2277,1439x2560&from=bu&u=Fg1KXoMnZfMOt4Z1e2eHVtmokNk1J484f6VpUvs1Jdw&cs=1439x0"],
        "gradient": "linear-gradient(to bottom, #000000, #8e44ad, #000000)",
        "layout": "left-text"
    },
    {
        "title": "Примеры сердец",
        "text": "Блок 2: сетка 2×2. Все карточки одинаковые.",
        "images": [
            "https://sun9-69.userapi.com/s/v1/ig2/wFGbIQY9pPer2rBBYi5qgvaP_tJgGRTceL7LUpLLkS-Y72U-9dAa52QQEJNGovC1PZ72mAj0aRwyot7BwKLVX2Hm.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1440x1920,1920x2560&from=bu&u=suh2sLFSC4ZCWU-6sI6U_peB1Ur_nGXMNz-SDkmzP94&cs=1920x0",
            "https://sun9-25.userapi.com/s/v1/ig2/mZ9b-IAX3KyLX26H9yzqZWRncRYlHUL5xHrDMwgstX2JdKmtn2KvcS-HNzyx4N-C0qq66cPPHQjG-2cy5aYJixXx.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1440x1920,1920x2560&from=bu&cs=1920x0",
            "https://sun9-42.userapi.com/s/v1/ig2/EE5xhP6aTPjm9SjKRgMfurYuRoshciN_hHMcVifpptJ8BiyvIUFsvoWdd4Uv9GhuApplUesIyu7q5JQjMGeL9I6r.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1440x1920,1920x2560&from=bu&cs=1920x0",
            "https://sun9-66.userapi.com/s/v1/ig2/6rdP5RCAaeufZioNztltMuNtI1ru8fBwVqi98NRabzfnjxeFWsGAqzwD5iYDch550W3RS5d4iTW92V1ZlPWHGOuF.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1440x1920,1920x2560&from=bu&u=DwjyEllJAyjLb524sg4vjIFPgQ6YyldtL0Y29d3Pufg&cs=1920x0"
        ],
        "gradient": "linear-gradient(to bottom, #000000, #1abc9c, #000000)",
        "layout": "top-text-grid-2x2"
    },
    {
        "title": "Изделия актуальны уже сейчас!",
        "text": "Работы есть",
        "images": ["https://sun9-75.userapi.com/s/v1/ig2/5Md57iId7L9yFbn4a1YORMbwIegGxMp-muu3FkvjZtvPRldEDmQij9M2M1hZEZxAf4fprgLJDCsBUEZQbuTnNlcX.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1440x1920,1920x2560&from=bu&cs=1920x0"],
        "gradient": "linear-gradient(to bottom, #000000, #3498db, #000000)",
        "layout": "right-text"
    },
    {
        "title": "Остальные работы",
        "text": "Блок 4: ряд из 3 картинок. Теперь они в таких же карточках, как в других блоках.",
        "images": [
            "https://sun9-47.userapi.com/s/v1/ig2/QfbGR5VBN9-4MsHAAvwh5zoV4RzgLhuK9OsN3Hbhxc7Hij1h3jn7v_r0FgKhwoF20_jNlL7mdFHrpY_514HdpyCE.jpg?quality=95&as=32x57,48x85,72x128,108x192,160x285,240x427,360x640,480x854,540x961,640x1139,720x1281,1080x1921,1280x2277,1439x2560&from=bu&cs=1439x0",
            "https://sun9-27.userapi.com/s/v1/ig2/BxNhj4IGTW5jZKiKBriE1o-GDTZqyGp_ssHngUUxD6ZYkt0LDNsmxr42xcf_XmmxRy1fQfuIzENwyxpmRNn89Rr3.jpg?quality=95&as=32x57,48x85,72x128,108x192,160x285,240x427,360x640,480x854,540x961,640x1139,720x1281,1080x1921,1280x2277,1439x2560&from=bu&cs=1439x0",
            "https://sun9-72.userapi.com/s/v1/ig2/-XqCxxrPI2bkU0cH5MnyMhiSTDxCF3T_9Aq-B9N6LGsFAK9JFAxlate-DGyJzZ9I-rJGfqfCcpCHiyRifP-fBH0_.jpg?quality=95&as=32x57,48x85,72x128,108x192,160x285,240x427,360x640,480x854,540x961,640x1139,720x1281,1080x1921,1280x2277,1439x2560&from=bu&cs=1439x0"
        ],
        "gradient": "linear-gradient(to bottom, #000000, #e67e22, #000000)",
        "layout": "center-text-row"
    },
    {
        "title": "Остальные работы",
        "text": "Блок 4: ряд из 3 картинок. Теперь они в таких же карточках, как в других блоках.",
        "images": [
            "https://sun9-47.userapi.com/s/v1/ig2/QfbGR5VBN9-4MsHAAvwh5zoV4RzgLhuK9OsN3Hbhxc7Hij1h3jn7v_r0FgKhwoF20_jNlL7mdFHrpY_514HdpyCE.jpg?quality=95&as=32x57,48x85,72x128,108x192,160x285,240x427,360x640,480x854,540x961,640x1139,720x1281,1080x1921,1280x2277,1439x2560&from=bu&cs=1439x0",
            "https://sun9-27.userapi.com/s/v1/ig2/BxNhj4IGTW5jZKiKBriE1o-GDTZqyGp_ssHngUUxD6ZYkt0LDNsmxr42xcf_XmmxRy1fQfuIzENwyxpmRNn89Rr3.jpg?quality=95&as=32x57,48x85,72x128,108x192,160x285,240x427,360x640,480x854,540x961,640x1139,720x1281,1080x1921,1280x2277,1439x2560&from=bu&cs=1439x0",
            "https://sun9-72.userapi.com/s/v1/ig2/-XqCxxrPI2bkU0cH5MnyMhiSTDxCF3T_9Aq-B9N6LGsFAK9JFAxlate-DGyJzZ9I-rJGfqfCcpCHiyRifP-fBH0_.jpg?quality=95&as=32x57,48x85,72x128,108x192,160x285,240x427,360x640,480x854,540x961,640x1139,720x1281,1080x1921,1280x2277,1439x2560&from=bu&cs=1439x0"
        ],
        "gradient": "linear-gradient(to bottom, #000000, #e67e22, #000000)",
        "layout": "center-text-row"
    }

]

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Все карточки картинок одинаковые</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
      background: #0f0f12;
      color: #e0e0e0;
    }

    .section-block {
      max-width: 1200px;
      width: 100%;
      margin: 0 auto;
      padding: 60px 20px;
      box-sizing: border-box;
      opacity: 0;
      animation: fadeInSection 0.8s ease-out forwards;
    }

    {% for i in range(blocks|length) %}
    .section-block:nth-child({{ i + 1 }}) {
      animation-delay: {{ 0.2 * i }}s;
    }
    {% endfor %}

    p {
      font-size: 1.1rem;
      color: rgba(255, 255, 255, 0.95);
      line-height: 1.5;
      margin: 0;
    }

    .hero-title {
      font-size: clamp(2rem, 5vw, 3rem);
      line-height: 1.1;
      margin: 0 0 16px 0;
      letter-spacing: -1px;
    }

    /* Блок 1 */
    .layout-left-text {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 60px;
    }
    .layout-left-text .hero-text { flex: 1; min-width: 300px; }
    .layout-left-text .hero-image-wrapper { flex: 1; min-width: 300px; }

    /* Блок 2 */
    .layout-top-text-grid-2x2 {
      display: flex;
      flex-direction: column;
      gap: 40px;
    }
    .layout-top-text-grid-2x2 .hero-images-wrapper {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
      width: 100%;
      box-sizing: border-box;
      align-items: start;
    }

    /* Блок 3 */
    .layout-right-text {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 60px;
    }
    .layout-right-text .hero-image-wrapper { flex: 1; min-width: 300px; }
    .layout-right-text .hero-text { flex: 1; min-width: 300px; text-align: right; }

    /* Блок 4 */
    .layout-center-text-row {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 40px;
      text-align: center;
    }
    .layout-center-text-row .hero-images-wrapper {
      display: grid;
      /* auto-fit даёт адаптивность, но карточки внутри — одинаковые */
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      width: 100%;
      box-sizing: border-box;
      align-items: start;
    }

    /* --- ЕДИНЫЙ СТИЛЬ КАРТОЧЕК (для всех блоков) --- */
    .hero-image-item, .hero-image-wrapper {
      position: relative;
      overflow: hidden;
      border-radius: 20px;
      box-shadow: 0 30px 60px rgba(0,0,0,0.5);
      width: 100%;
    }

    .hero-image-item img, .hero-image-wrapper img {
      width: 100%;
      height: auto;
      display: block;
      aspect-ratio: 9 / 16;   /* пропорции под твои размеры */
      object-fit: cover;     /* заполняем, лишнее обрезаем */
      filter: brightness(75%);
      transition: filter 1s cubic-bezier(0.25, 1, 0.5, 1);
    }

    .hero-image-item:hover img, .hero-image-wrapper:hover img {
      filter: brightness(110%);
    }

    @keyframes fadeInSection {
      to { opacity: 1; transform: none; }
    }

    @media (max-width: 768px) {
      .layout-left-text, .layout-right-text {
        flex-direction: column;
        align-items: stretch;
      }
      .layout-right-text .hero-text { text-align: left; }
      .layout-top-text-grid-2x2 .hero-images-wrapper,
      .layout-center-text-row .hero-images-wrapper {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>

  {% for block in blocks %}
  <section class="section-block layout-{{ block.layout }}" style="background: {{ block.gradient }};">

    {% if block.layout == "top-text-grid-2x2" or block.layout == "center-text-row" %}
      <div class="hero-text">
        <h1 class="hero-title">{{ block.title }}</h1>
        <p>{{ block.text }}</p>
      </div>

      <div class="hero-images-wrapper">
        {% for img_url in block.images %}
        <!-- Карточка картинки (одинакова для всех блоков) -->
        <div class="hero-image-item">
          <img src="{{ img_url }}" alt="{{ block.title }}">
        </div>
        {% endfor %}
      </div>

    {% elif block.layout == "left-text" or block.layout == "right-text" %}
      {% if block.layout == "left-text" %}
        <div class="hero-text">
          <h1 class="hero-title">{{ block.title }}</h1>
          <p>{{ block.text }}</p>
        </div>
        <!-- Одиночная картинка тоже в такой же карточке -->
        <div class="hero-image-wrapper">
          <img src="{{ block.images[0] }}" alt="{{ block.title }}">
        </div>
      {% else %}
        <div class="hero-image-wrapper">
          <img src="{{ block.images[0] }}" alt="{{ block.title }}">
        </div>
        <div class="hero-text">
          <h1 class="hero-title">{{ block.title }}</h1>
          <p>{{ block.text }}</p>
        </div>
      {% endif %}
    {% endif %}

  </section>
  {% endfor %}

</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML, blocks=blocks)

if __name__ == "__main__":
    app.run(debug=True)
