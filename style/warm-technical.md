# Warm Technical: video grafikos stilius

Išsaugota 2026-11-20. Šis stilius taikomas visai ai-eng-lab video grafikai
(motion graphics, schemoms, titulinėms kortelėms, thumbnail'ams). Prieš
kuriant bet kokią video grafiką, pirma perskaityk šį failą ir pažiūrėk
`refs/` paveikslėlius.

Video proporcija: **apie 70 % tikras ekrano vaizdas** (kodas, terminalas,
svetainės, dokumentacija), **apie 30 % grafika** šiuo stiliumi. Formatas
16:9, 1920×1080.

## Nuorodos (`refs/`)

| Failas | Kas jame |
| --- | --- |
| `palette.png` | Pagrindinė paletė ir proporcijos. Atkurta iš tavo atsiųsto paveikslėlio pagal hex reikšmes (originalas buvo pokalbyje, ne faile). |
| `slideboard-architecture.png` | Keturi kadrai: „Let's build an agent“ (kodo langas + sąrašas), „RAG Architecture“ (srauto plytelės), „From data to insights“ (duomenų vizualizacija), „Find the right context“ (paieškos langas). |
| `storyboard-rag.png` | Keturi kadrai: „How RAG works“ (srautas su grįžtamąja rodykle), kodo langas su 3D duomenų baze, embeddings → vector DB, pokalbio UI. |
| `workflows-agents.png` | Keturi kadrai: „How RAG works“, „AI Agent Workflow“ (punktyrinė grįžtamoji rodyklė su etikete), programos UI (Keepmi), kodo langas su robotu. Rastas Downloads kartu su kitais dviem, to paties stiliaus. |

## Paletė

Hex reikšmės yra pagrindinis šaltinis.

| Pavadinimas | Hex | Kam |
| --- | --- | --- |
| Warm Canvas | `#F5F3EE` | Vaizdo fonai |
| Deep Ink | `#202522` | Tekstas, tamsios kortelės (kodo langai, tamsūs mygtukai) |
| Mint Teal | `#12BFA5` | Pagrindinis akcentas |
| Soft Coral | `#FF754E` | Dėmesio akcentai |
| Lavender | `#B99AEF` | Antriniai elementai |
| Muted Sage | `#DCE4E0` | Linijos, foninės sritys |

**Proporcijos:** 65 % neutralios erdvės, 20 % tamsių elementų, 10 %
pagrindinių akcentų (mint), 5 % papildomų akcentų (coral, lavender).

### Atspalviai iš pavyzdžių

Pavyzdžiuose akcentai beveik niekada nebūna ryškūs dideliuose plotuose:
plytelės ir piliulės yra šviesūs atspalviai, o pilna spalva lieka mažiems
elementams (kvadratėliams, ikonoms, varnelėms). Spalvos paimtos iš
`workflows-agents.png` pikselių, todėl apytikslės:

| Kur | Spalva |
| --- | --- |
| Puslapio fonas (šiltesnis, persikinis) | `#FCF4EC` |
| Kortelės fonas | `#FDF5EC` |
| Balta plytelė | `#FFFBF8` |
| Mint plytelė | `#C9F0E0` |
| Mint piliulė (pilnesnė) | `#85E8C7` |
| Status piliulė „Published“ | `#D9F3E6` |
| Levandų plytelė | `#F1D8F5` |
| Persikinė (coral) plytelė | `#FEB792` |
| Persikinė piliulė / aktyvus meniu punktas | `#FDE0BA` / `#FEDEC0` |
| Mažas oranžinis kvadratėlis | `#FD8E51` |
| Mažas teal kvadratėlis | `#35BDA4` |
| Mažas levandų kvadratėlis | `#DAC1F6` |
| Kodo lango fonas / viršutinė juosta | `#272626` / `#3C3E3D` |

Pastaba: tavo paletėje fonas yra neutralesnis (`#F5F3EE`), o pavyzdžiuose
šiltesnis ir persikinis su coral švytėjimu kampuose. Siūlau bazę imti
`#F5F3EE`, o šilumą duoti švytėjimu (žr. žemiau). Jei nori šiltesnio fono,
nuspręsk.

## Kompozicija

- **Fonas:** Warm Canvas, kampuose dideli labai išblukę coral / persikiniai
  apskritimai (radial glow, apie 10–20 % ryškumo). Kartais kampe išblukęs
  taškų tinklelis (dot grid).
- **Kortelės:** didelės, labai apvalintos (apie 48–56 px spindulys esant
  1920 px pločiui), šviesios, su minkštu šiltu šešėliu (didelis blur, maža
  intensyvumas). Ryškių kraštinių nėra.
- **Daug tuščios erdvės.** Kadre vienas pagrindinis dalykas.
- **Antraštės blokas kairėje viršuje:**
  1. *breadcrumb* piliulė: balta, apvali, tekstas „Tema / 01“ (pvz.,
     „AI Basics / 01“, „RAG / 01“). Puikiai tinka skyriaus numeriui
     („LLM Basics / 03“);
  2. didelė, labai stora antraštė (Deep Ink), viena ar dvi eilutės,
     glaudus tarpas tarp eilučių;
  3. paantraštė normalaus storio, pilkšvai tamsi.
- **Centruota antraštė** (alternatyva): virš jos maža piliulė su coral
  kontūru („RAG“), po antrašte trumpas coral brūkšnys.

## Komponentai

- **Srauto plytelės:** 4 apvalūs kvadratai iš eilės, kiekvienas kito
  atspalvio (balta → mint → levandų → persikinė). Viduje ikona, stora
  etiketė ir 1–2 eilučių aprašas. Tarp plytelių ploni tamsūs „→“.
- **Grįžtamoji rodyklė:** plona linija po plytelėmis su piliule centre
  (mint fonas, tamsus apskritimas su varnele, tekstas „Context-aware
  response“).
- **Punktyrinė jungtis** su etikete piliulėje virš jos („Feedback &
  Iterate“, persikinis fonas).
- **Sąrašas su varnelėmis:** mint apskritimas su balta varnele + tekstas.
- **Kodo langas:** tamsi kortelė (Deep Ink), macOS taškai (raudonas,
  geltonas, žalias), monospace šriftas. Sintaksės spalvos: raktažodžiai
  mėlyni / levandų, eilutės (strings) coral, funkcijų vardai šiltai
  geltoni, likęs tekstas šviesiai pilkas. Svarbus fragmentas paryškinamas
  rusvu fonu (kaip `vectorDb.search` pavyzdyje).
- **Programos / naršyklės langas:** šviesi kortelė su macOS taškais,
  adreso juosta, šoninis meniu (aktyvus punktas persikiniame fone),
  paieškos laukas, rezultatų eilutės su „Top result“ mint piliule.
- **Teksto vietoje pilkos juostelės** (skeleton) neesminiam tekstui.
- **Pokalbio UI:** vartotojo burbulas dešinėje šviesiai pilkas su avataru,
  asistento atsakymas kairėje su mint žvaigždute (sparkle).
- **Būsenos piliulės:** mint („Published“), levandų („Draft“), persikinė
  („Ready“).
- **Tamsus mygtukas:** Deep Ink fonas, baltas tekstas, apvalūs kampai.
- **Patarimo kortelė:** persikinis fonas, lemputės ikona, 2 eilutės teksto.
- **Duomenų vizualizacija:** pilki taškai → mint kvadratėlių tinklelis →
  stulpeliai (mint ir coral) su linija baltoje kortelėje.
- **Dekoracijos:** maži apvalūs kvadratėliai (mint, coral, levandų, sage)
  kortelių kampuose; 4 kampų žvaigždutės (teal ir coral); trumpi coral
  brūkšneliai („spindulys“) šalia svarbaus elemento; išlenktos punktyrinės
  rodyklės.
- **Ikonos:** paprastos, užpildytos, apvalių formų (pokalbio burbulas,
  didinamasis stiklas, užrašų lenta, žvaigždutė, žmogus, smegenys,
  duomenų bazė, žaibas, taikinys).
- **3D objektai:** minkšti, mint atspalvių (duomenų bazės cilindras,
  plaukiojantys dokumentai), švelnūs šešėliai. Baltas robotas su tamsiu
  ekranu ir mint akimis (naudoti saikingai).

## Tipografija (iš akies, patvirtinti)

- Antraštės: geometrinis sans-serif, labai storas (700–800). Artimi
  variantai: **Inter**, **Plus Jakarta Sans** arba **Manrope** (visi
  nemokami Google Fonts).
- Tekstas: tas pats šriftas, 400–500 storis.
- Kodas: monospace, pvz., **JetBrains Mono**.
- Apytiksliai dydžiai esant 1920×1080: antraštė 120–150 px, paantraštė
  apie 56 px, plytelės etiketė apie 40 px, aprašas apie 30 px, piliulės
  apie 30 px.

## Judesys (pavyzdžiuose jo nėra, tai siūlymas)

- Elementai atsiranda švelniai: išryškėja ir pakyla 20–30 px, spyruoklinis
  (spring) judesys be stipraus atšokimo.
- Srauto plytelės pasirodo paeiliui (stagger), rodyklės „nusipiešia“.
- Dekoratyvūs kvadratėliai lėtai plūduriuoja.
- Ekrano įrašai įkomponuojami į šviesią kortelę su macOS taškais, kad
  tikras vaizdas ir grafika atrodytų kaip viena visuma.

## Ko vengti

- Tamsių fonų visam kadrui (tamsios tik kortelės).
- Ryškių akcentų dideliuose plotuose.
- Daug elementų viename kadre.
- Neoninių švytėjimų, gradientinio teksto.

## CSS kintamieji

```css
:root {
  --canvas: #F5F3EE;
  --canvas-warm: #FCF4EC;
  --card: #FFFBF8;
  --ink: #202522;
  --mint: #12BFA5;
  --mint-tint: #C9F0E0;
  --coral: #FF754E;
  --coral-tint: #FEB792;
  --peach-tint: #FDE0BA;
  --lavender: #B99AEF;
  --lavender-tint: #F1D8F5;
  --sage: #DCE4E0;
  --code-bg: #272626;
  --code-bar: #3C3E3D;
}
```

## Atviri klausimai

- Kuris šriftas?
- Kuo daryti 16:9 grafiką: tiesiogiai Remotion ar TikMaker su 16:9 (A
  kelias, žr. PLAN.md)?
- Ar naudoti robotą kaip kanalo personažą?
