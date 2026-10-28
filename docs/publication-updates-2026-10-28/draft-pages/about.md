---
permalink: /
title: "About Me"
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

<section class="hero-panel about-hero">
  <h1>About Me</h1>
  <p>Hello there! I am Xun (Sean) Zhang, a first-year Ph.D. student in the <a href="https://www.duffield.cornell.edu/cee/">School of Civil and Environmental Engineering</a> at Cornell University. I work with <a href="https://www.duffield.cornell.edu/people/stefano-galelli/">Prof. Stefano Galelli</a> in the <a href="https://galelli.cee.cornell.edu/">Critical Infrastructure Systems Lab</a>.</p>
  <p>Before joining Cornell, I received my master's degree from the <a href="https://geohyd.tongji.edu.cn/index.htm">Department of Geological and Hydraulic Engineering, College of Civil Engineering</a> at <a href="https://www.tongji.edu.cn/">Tongji University</a> in June 2025. After graduation, I continued to work in the same department as a Research Assistant for one year. I earned my bachelor's degree in Hydraulic and Hydropower Engineering from the <a href="https://sjxy.nwsuaf.edu.cn/">College of Water Resources and Architectural Engineering</a> at <a href="https://www.nwafu.edu.cn/">Northwest A&amp;F University</a>. My academic training has shaped a broad interest in hydrogeology, hydrology, computational modeling, and data-driven methods.</p>
  <p>I am currently participating in the <a href="https://dareproject.org/">DARE project</a>, which is developing a global time-series dataset of river systems under human influence from 1950 onward.</p>
  <p>I look forward to continuing my research at Cornell and welcome discussions, collaborations, and research opportunities.</p>
  <div class="hero-actions">
    <a class="highlight-chip" href="mailto:xz2237@cornell.edu">E-mail: xz2237@cornell.edu</a>
  </div>
</section>

<section class="section-block about-interests">
  <h2>Current Research Interest</h2>
  <p class="section-lede">My current research interests focus on assessing how human interventions shape river systems. I am also interested in exploring innovative AI approaches to better represent human activities and characterize their impacts on rivers.</p>

  <details class="interest-details">
    <summary>Representative directions I have explored</summary>
    <div class="interest-grid">
      <section class="interest-block">
        <h3>Methods explored</h3>
        <p><strong>Inverse problems and inference:</strong> data assimilation; parameter estimation; uncertainty quantification; interpolation and reconstruction; causal inference; and geostatistics.</p>
        <p><strong>Generative and efficient modelling:</strong> generative models including DDPM, VAE, GAN, and flow matching; surrogate modelling; reduced-order modelling; and operator learning.</p>
        <p><strong>Scientific machine learning:</strong> physics-informed learning; transfer learning; reinforcement learning; graph learning; federated machine learning; and interpretable machine learning using SHAP and Grad-CAM.</p>
        <p><strong>Forecasting and process modelling:</strong> time-series forecasting with ARIMA, XGBoost/LightGBM, and GRU/LSTM/Transformer; upscaling methods for geologic models; and coupled surface water-groundwater modelling.</p>
      </section>
      <section class="interest-block">
        <h3>Application areas</h3>
        <p><strong>Groundwater modelling:</strong> groundwater contamination source identification; high-resolution characterization of hydraulic conductivity fields; groundwater well placement optimization; groundwater level prediction; and inversion of groundwater storage from satellite gravimetry.</p>
        <p><strong>Hydrology and environmental modelling:</strong> urban flooding; debris floods; computational fluid dynamics; atmospheric pollution modelling; and Arctic sea ice.</p>
        <p><strong>Remote sensing and image analysis:</strong> image-based sediment detection and remote sensing for lake carbon sources and sinks.</p>
        <p><strong>Other physical and engineering systems:</strong> seismic waveform inversion; structural health monitoring; inverse design of materials; and battery state estimation.</p>
      </section>
    </div>
  </details>

</section>

<section class="section-block academic-service">
  <h2>Academic Service</h2>
  <details class="interest-details">
    <summary>Journal reviewer</summary>
    <p>Reviewer for <em>Hydrogeology Journal</em>, <em>Journal of Hydrology</em>, and <em>Water Resources Research</em>.</p>
  </details>
</section>

<section class="news-latest">
  <div class="news-heading">
    <h2>News (latest)</h2>
    <a class="all-news-link" href="{{ '/news/' | relative_url }}">All News</a>
  </div>
  <div class="news-list">
    {% capture homepage_news_source %}{% include_relative news.md %}{% endcapture %}
    {% include latest-news.html content=homepage_news_source %}
  </div>
  <p class="site-updated">Last updated: October 28, 2026</p>
</section>
