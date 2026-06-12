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
  <h1>About me</h1>
  <p>Hello there! I am Xun (Sean) Zhang, an incoming Ph.D. student in the <a href="https://www.duffield.cornell.edu/cee/">School of Civil and Environmental Engineering</a> at Cornell University.</p>
  <p>Before joining Cornell, I received my master's degree from the <a href="https://geohyd.tongji.edu.cn/index.htm">Department of Geological and Hydraulic Engineering, College of Civil Engineering</a> at <a href="https://www.tongji.edu.cn/">Tongji University</a> in June 2025. After graduation, I continued to work in the same department as a Research Assistant for one year. I earned my bachelor's degree in Hydraulic and Hydropower Engineering from the <a href="https://sjxy.nwsuaf.edu.cn/">College of Water Resources and Architectural Engineering</a> at <a href="https://www.nwafu.edu.cn/">Northwest A&amp;F University</a>. My academic training has shaped a broad interest in hydrogeology, hydrology, computational modeling, and data-driven methods for understanding subsurface flow and transport processes.</p>
  <p>I look forward to continuing my research at Cornell and welcome discussions, collaborations, and research opportunities.</p>
  <div class="hero-actions">
    <a class="highlight-chip" href="mailto:xz2237@cornell.edu">E-mail: xz2237@cornell.edu</a>
    <span class="highlight-chip highlight-chip--soft">Open to collaboration</span>
  </div>
</section>

<section class="section-block about-interests">
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

</section>

<section class="news-latest">
  <div class="news-heading">
    <h2>News (latest)</h2>
    <a class="all-news-link" href="{{ '/news/' | relative_url }}">All News</a>
  </div>
  <div class="news-list">
    <article class="news-item">
      <div class="news-date">2025.12</div>
      <p class="news-copy">I co-developed <strong>PIS</strong> with my collaborator Weijie Yang for broad physical parameter estimation. This work proposes a unified perspective for PDE-constrained parameter estimation problems: an end-to-end solver based on diffusion models. <a href="https://doi.org/10.13140/RG.2.2.23577.68963">[View Paper]</a></p>
    </article>
    <article class="news-item">
      <div class="news-date">2025.11</div>
      <div>
        <p class="news-copy">I developed <strong>Diffusion-Inversion-Net (DIN)</strong>: An End-to-End Direct Probabilistic Framework for Characterizing Hydraulic Conductivities and Quantifying Uncertainty.<br>Open source code: <a href="https://github.com/XunZhangSean/Diffusion-Inversion-Net">XunZhangSean/Diffusion-Inversion-Net</a>.</p>
        <details class="news-note">
          <summary>👇 Read the story behind this research (Research Note)</summary>
          <p>This is an idea I initially conceived two years ago when I was first introduced to data assimilation and generative models. This study leverages the iterative denoising advantage and probabilistic generation characteristics of diffusion models to build an end-to-end inversion solver for the fine-scale characterization of groundwater contamination sites. There are still imperfections in the paper that need to be addressed in the future.</p>
          <p>I sincerely thank my collaborator, <strong>Weijie Yang</strong> from UCB, for completing this "dream work" with me, and I also extend my gratitude to Prof. Jiang and Prof. Zhang for their guidance.</p>
          <p><em>A personal reflection:</em> I actually felt a "small disappointment" after finishing this. The findings differed from my intuition two years ago. I initially hoped that the Diffusion model could theoretically prove its equivalence with Data Assimilation. However, while the iterative update in the Kalman Filter and the conditional iterative denoising in Diffusion models are intuitively similar (both embodying the idea of Bayesian correction), there seems to be no direct mathematical link. The Kalman Filter corrects predictions via new observations; Diffusion models correct sampling trajectories via predicted noise. Although I couldn't bridge this gap, I hope future theorists might connect them—that would be fascinating!</p>
        </details>
      </div>
    </article>
    <article class="news-item">
      <div class="news-date">2025.07</div>
      <p class="news-copy">Our collaborative paper on remote sensing data and carbon sources/sinks was published in Remote Sensing. My <a href="https://doi.org/10.3390/rs17142475">third paper</a> is now online. Click to view.</p>
    </article>
  </div>
</section>
