#!/usr/bin/env python3
"""Generate partials/publications.qmd with type badges and highlighted author name."""

ME_EN = "Shim, D."
ME_KO = "심동녘"

# (badge_type, raw_citation)  -- citation uses {ME} where the author's name appears
intl = [
    ("SSCI",  "Choi, Y., {ME}, Park, Y., & Lee, C. (2025). Gamification in the Metaverse: How Design Attributes Shape User Preferences Across Age Groups. <i>Journal of Theoretical and Applied Electronic Commerce Research, 20</i>(4), 310. https://doi.org/10.3390/jtaer20040310"),
    ("SSCI",  "{ME} (2025). Journey from light viewer to heavy viewer when you get engaged in OTT: a Hidden Markov Model approach. <i>Journal of Media Economics</i>, 1–21. https://doi.org/10.1080/08997764.2025.2535329"),
    ("Scopus","Kang, S., Altmann, J., & {ME} (2025). Consumer Insights from South Korea&rsquo;s Publicly Accredited e-Payment Electronic Certification System by Evaluating Security Preferences and Willingness to Pay. <i>International Journal of Networked and Distributed Computing, 13</i>, 24. https://doi.org/10.1007/s44227-025-00064-1"),
    ("SCI",   "{ME} (2025). Quantifying Social Benefits of Virtual Power Plants (VPPs) in South Korea: Contingent Valuation Method. <i>Energies, 18</i>(12), 3006."),
    ("SSCI",  "{ME}, Choi, Y., & Lee, C. (2025). Exploring the competitive market structure of digital-based subscription economy: The empirical investigation of South Korea. <i>Telematics and Informatics, 98</i>, 102264."),
    ("SSCI",  "Kim, K., Maliphol, S., {ME}, & Lee, C. (2024). Exploring the interplay between social distancing, innovation adoption, and privacy concerns amid the COVID-19 crisis. <i>Science and Public Policy, 51</i>(6), 1257&ndash;1266."),
    ("SSCI",  "{ME} (2024). Interplay between Platform Providers and Complementors via Affordance, Autonomy, and Super-Modularity: The Empirical Investigation of the Korean Digital Industry. <i>Journal of Theoretical and Applied Electronic Commerce Research, 19</i>(2), 975&ndash;992."),
    ("SSCI",  "Choi, H., {ME}, & Kim, S. W. (2024). Heterogeneous public preferences for undergrounding high-voltage power transmission lines: The case of Seoul metropolitan area in South Korea. <i>Energy Economics, 132</i>, 107448."),
    ("SSCI",  "{ME}, Choi, H., & Kim, S. W. (2024). Heterogeneous public attitudes toward high-voltage power transmission lines and willingness to pay for undergrounding projects. <i>Energy &amp; Environment, 35</i>(7), 3736&ndash;3758."),
    ("SSCI",  "{ME}, Lee, C., & Oh, I. (2022). Analysis of OTT Users&rsquo; Watching Behavior for Identifying a Profitable Niche: Latent Class Regression Approach. <i>Journal of Theoretical and Applied Electronic Commerce Research, 17</i>(4), 1564&ndash;1580."),
    ("SSCI",  "{ME} (2021). Capturing heterogeneous decision making processes: The case with the E-book reader market. <i>International Journal of Market Research, 63</i>(2), 216&ndash;235."),
    ("SSCI",  "Hwang, W. S., & {ME} (2021). Measuring the impact of ICT-driven product and process innovation on the Korean economy. <i>Global Economic Review, 50</i>(3), 235&ndash;253."),
    ("SSCI",  "Oh, I., & {ME} (2020). IT adoption and sustainable growth of firms in different industries&mdash;are the benefits still expected? <i>Sustainability, 12</i>(22), 9689."),
    ("SSCI",  "Oh, S., {ME}, & Lee, D. (2020). Evaluation of complementarity effect of innovation policies: Venture certification and Inno-biz certification in Korea. <i>The Singapore Economic Review, 65</i>(02), 385&ndash;402."),
    ("SSCI",  "{ME}, Shin, J., & Kwak, S. Y. (2018). Modelling the consumer decision-making process to identify key drivers and bottlenecks in the adoption of environmentally friendly products. <i>Business Strategy and the Environment, 27</i>(8), 1409&ndash;1421."),
    ("SSCI",  "{ME}, Kim, S. W., Altmann, J., Yoon, Y. T., & Kim, J. G. (2018). Key features of electric vehicle diffusion and its impact on the Korean power market. <i>Sustainability, 10</i>(6), 1941."),
    ("SSCI",  "{ME}, Kim, S. W., & Altmann, J. (2018). Strategic management of residential electric services in the competitive market: Demand-oriented perspective. <i>Energy &amp; Environment, 29</i>(1), 49&ndash;66."),
    ("SSCI",  "{ME}, Kim, J. G., & Altmann, J. (2016). Strategic management of R&amp;D and marketing integration for multi-dimensional success of new product developments: an empirical investigation in the Korean ICT industry. <i>Asian Journal of Technology Innovation, 24</i>(3), 293&ndash;316."),
    ("SSCI",  "{ME}, Kim, J. G., & Altmann, J. (2016). Identifying key drivers and bottlenecks in the adoption of E-book readers in Korea. <i>Telematics and Informatics, 33</i>(3), 860&ndash;871."),
    ("SSCI",  "Yeo, Y., {ME}, Lee, J. D., & Altmann, J. (2015). Driving forces of CO<sub>2</sub> emissions in emerging countries: LMDI decomposition analysis on China and India&rsquo;s residential sector. <i>Sustainability, 7</i>(12), 16108&ndash;16129."),
]

kci = [
    "김성윤, 최동환, {ME}. (2025). 시험인증산업에서 기밀보안성과 전문성에 대한 수요기업 선호 분석과 서비스 고도화 방안. <i>산업연구, 9</i>(2), 66&ndash;99.",
    "최동환, 김성윤, 김슬하, {ME}. (2025). 시험·인증 서비스 수요기업 선호 분석: 신속성, 편의성 및 해외인증 컨설팅을 중심으로. <i>서비스 연구, 15</i>(2), 1&ndash;19.",
    "김성윤, {ME}. (2024). 고안전 융합제품 개발산업의 소프트웨어(SW) 안전 수준 제고를 위한 정책수단의 상대적 중요도 평가. <i>한국혁신학회지, 19</i>(4), 217&ndash;247.",
    "김태균, {ME}. (2024). 조건부가치측정법(CVM)을 활용한 지능형 CCTV 플랫폼의 편익 추정 연구. <i>산업융합연구, 22</i>(7), 1&ndash;13.",
    "방효민, {ME}. (2024). 패션·의류 신제품 개발에서 기능 부서 간 협업이 신제품 성과에 미치는 영향. <i>상품학연구, 42</i>(2), 57&ndash;64.",
    "{ME}, 인혁준. (2023). AI 채용 시스템의 공정성, 신뢰성, 혁신특성이 이용자의 태도에 미치는 영향. <i>상품학연구, 41</i>(5), 49&ndash;58.",
    "{ME}. (2023). Heckman 2단계 모형을 활용한 주말과 주중 OTT 시청시간결정요인 비교 분석. <i>한국혁신학회지, 18</i>(3), 89&ndash;108.",
    "방효민, {ME}. (2023). 패션·의류 신제품개발 프로젝트에서 자원 적합성이 시장적기출시와 제품혁신성에 미치는 영향. <i>글로벌경영학회지, 20</i>(3), 105&ndash;129.",
    "고동환, {ME}. (2022). 중국경제 구조조정과 첨단기술 육성전략에 따른 한국 ICT 수출의 구조적 단절 연구. <i>한국혁신학회지, 17</i>(4), 69&ndash;84.",
    "방효민, {ME}. (2022). 패션기업 디지털전환 성공요인 및 이행전략의 중요도 평가. <i>글로벌경영학회지, 19</i>(5), 1&ndash;25.",
    "이종서, {ME}. (2022). 잠재계층분석(LCA)을 활용한 가공송전선로 건설에 대한 인식과 태도의 유형 및 특성 연구. <i>환경정책, 30</i>(1), 93&ndash;115.",
    "{ME}, 고동환. (2022). 인공지능(AI) 기술도입에 따른 산업별 노동수요변화 탐색. <i>한국혁신학회지, 17</i>(1), 85&ndash;103.",
    "{ME}. (2021). 미디어이용자의 OTT 이용행태 결정요인 분석: 유료방송 시청요인과 이용자 혁신성향을 중심으로. <i>한국혁신학회지, 16</i>(3), 221&ndash;245.",
    "최현홍, {ME}. (2020). 텍스트마이닝을 적용한 ICT융합 트렌드 분석. <i>한국혁신학회지, 15</i>(3), 257&ndash;281.",
    "{ME}, 오승환. (2018). 연구개발특구가 입주기업에 미치는 영향에 관한 연구. <i>한국혁신학회지, 13</i>(1), 169&ndash;191.",
    "강송희, {ME}, 백필호. (2015). 소프트시스템 모델 방법론을 통해 진단한 국내 공개 SW 산업의 문제점과 정책전략 연구. <i>한국전자거래학회지, 20</i>(4), 193&ndash;208.",
    "오승환, {ME}, 김규남. (2015). 벤처인증정책과 이노비즈인증정책의 중복효과에 대한 연구: ICT산업을 중심으로. <i>기술혁신학회지, 18</i>(2), 358&ndash;386.",
    "{ME}, 김응도, 황준석. (2015). 소셜커머스에서 소비자 충동구매행위에 영향을 미치는 요인에 관한 연구. <i>글로벌경영학회지, 12</i>(1), 263&ndash;294.",
]

import re
def linkify(text):
    return re.sub(r'(https?://\S+)', r'<a href="\1" target="_blank" rel="noopener">\1</a>', text)

badge_class = {"SSCI": "b-ssci", "SCI": "b-sci", "Scopus": "b-scopus", "KCI": "b-kci"}

def render_item(badge, cite, name):
    cite = cite.replace("{ME}", f"<span class='pub-me'>{name}</span>")
    cite = linkify(cite)
    return (f'  <li class="pub-item">\n'
            f'    <span class="pub-badge {badge_class[badge]}">{badge}</span>\n'
            f'    <span class="pub-cite">{cite}</span>\n'
            f'  </li>')

out = []
out.append('<!-- AUTO-GENERATED publication list. Edit gen_pubs.py and re-run to update. -->')
out.append('')
out.append('::: {.pub-wrap}')
out.append('')
out.append(f'<p class="pub-summary"><span class="pub-stat"><strong>{len(intl)+len(kci)}</strong> peer-reviewed articles</span>'
           f'<span class="pub-stat"><strong>{len(intl)}</strong> international (SSCI / SCI / Scopus)</span>'
           f'<span class="pub-stat"><strong>{len(kci)}</strong> Korean (KCI)</span></p>')
out.append('')
out.append('### International Journals')
out.append('')
out.append('<ol class="pub-list">')
for badge, cite in intl:
    out.append(render_item(badge, cite, ME_EN))
out.append('</ol>')
out.append('')
out.append('### Korean Citation Index (KCI) Journals')
out.append('')
out.append('<ol class="pub-list">')
for cite in kci:
    out.append(render_item("KCI", cite, ME_KO))
out.append('</ol>')
out.append('')
out.append(':::')
out.append('')

with open("partials/publications.qmd", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("wrote partials/publications.qmd:", len(intl), "intl +", len(kci), "kci")
