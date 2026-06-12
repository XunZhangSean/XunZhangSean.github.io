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

<div class="hero-panel about-hero">
  <p class="hero-eyebrow">Research Assistant · Hydrogeology & Scientific Machine Learning</p>
  <h1>About me</h1>
  <p>Hello there! I'm Sean (Xun Zhang), a graduate of the College of Civil Engineering at Tongji University (June 2025), and currently a Research Assistant in the same department.</p>
  <p>My academic journey began with a Bachelor's degree in Hydraulic Engineering from Northwest A&F University, where I studied hydraulic engineering systems and their interactions with the environment. During my master's studies, I found a creative intersection between data science and hydrogeology. My research focuses on <strong>groundwater flow and solute transport modeling</strong>, especially deep learning-based parameterization methods (DLPMs) and surrogate models for predicting groundwater solute transport.</p>
  <p>I plan to pursue a PhD degree in the near future and welcome discussions, collaborations, and research opportunities.</p>
  <div class="hero-actions">
    <a class="highlight-chip" href="mailto:2232324@tongji.edu.cn">E-mail: 2232324[at]tongji[dot]edu[dot]cn</a>
    <span class="highlight-chip highlight-chip--soft">Open to collaboration</span>
  </div>
</div>

<div class="card-panel about-interests">
  <h2>Current Research Interest</h2>
  <p class="section-lede">I work around groundwater modelling, urban flooding, scientific machine learning, inverse problems, and data assimilation.</p>

  <div class="interest-grid">
    <section class="interest-block">
      <h3>Method focus</h3>
      <div class="interest-tags">
        <span>Data assimilation</span>
        <span>Inverse problems</span>
        <span>Generative modelling</span>
        <span>Surrogate modelling</span>
        <span>Physics-informed learning</span>
        <span>Uncertainty quantification</span>
      </div>
    </section>

    <section class="interest-block">
      <h3>Application focus</h3>
      <div class="interest-tags">
        <span>Groundwater contamination</span>
        <span>Hydraulic conductivity fields</span>
        <span>Groundwater level prediction</span>
        <span>Urban flooding</span>
        <span>Remote sensing</span>
        <span>Environmental modelling</span>
      </div>
    </section>
  </div>

  <details class="interest-details">
    <summary>Representative directions I have explored</summary>
    <p><strong>Methods side</strong>: parameter estimation; interpolation and reconstruction; DDPM, VAE, GAN, and flow matching; reduced-order modelling; operator learning; transfer learning; reinforcement learning; graph learning; federated machine learning; causal inference; geostatistics; time-series forecasting models including ARIMA, XGBoost/LightGBM, GRU/LSTM/Transformer; interpretable machine learning such as SHAP and Grad-CAM; upscaling methods for geologic models; and coupled surface water-groundwater modelling.</p>
    <p><strong>Applications side</strong>: groundwater contamination source identification and high-resolution characterization of hydraulic conductivity fields; groundwater well placement optimization; groundwater level prediction; urban flooding; computational fluid dynamics; atmospheric pollution modelling; seismic waveform inversion; structural health monitoring; inverse design of materials; battery state estimation; debris floods; inversion of groundwater storage from satellite gravimetry; image-based sediment detection; remote sensing for lake carbon sources and sinks; and Arctic sea ice.</p>
  </details>
    
</div>

<div class="card-panel about-links">
  <h2>Explore My Work</h2>
  <div class="quick-links-grid">
    <a class="quick-link-card" href="{{ '/news/' | relative_url }}">
      <span class="quick-link-title">🔥 News</span>
      <span class="quick-link-description">Recent research and activity updates</span>
    </a>
    <a class="quick-link-card" href="{{ '/publications/' | relative_url }}">
      <span class="quick-link-title">📝 Publications and Conferences</span>
      <span class="quick-link-description">Papers, preprints, and conference records</span>
    </a>
    <a class="quick-link-card" href="{{ '/hydro90/' | relative_url }}">
      <span class="quick-link-title">💧 Hydro90</span>
      <span class="quick-link-description">A hydrology knowledge project</span>
    </a>
    <a class="quick-link-card" href="{{ '/honors/' | relative_url }}">
      <span class="quick-link-title">🎖 Honors and Awards</span>
      <span class="quick-link-description">Selected recognitions and awards</span>
    </a>
    <a class="quick-link-card" href="{{ '/education/' | relative_url }}">
      <span class="quick-link-title">📖 Educations</span>
      <span class="quick-link-description">Academic training and experiences</span>
    </a>
  </div>
</div>
