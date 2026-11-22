# 1 tutorialo video planas: kaip veikia LLM pokalbių botas (1 dalis)

Juodraštis, atnaujinta 2026-11-20. Tai planas, ne scenarijus. Video bus
angliškas, todėl skyrių pavadinimai angliški (jie taps YouTube chapters).
Grafika daroma pagal [Warm Technical](../../style/warm-technical.md) stilių.

## Esmė

- **Sąžiningas rėmas.** Mokausi AI inžinerijos ir mokausi ant tikro
  projekto: kuriu pokalbių botą savo nedidelės web studijos Codeart
  svetainei. Codeart yra pavyzdys, ne skubus verslo poreikis. Video
  nesakome, kad botas „labai reikalingas“.
- **Ką botas daro:** išklausinėja lankytoją apie jo projektą ir pateikia
  preliminarią kainą ir terminą pagal Codeart kainas. Atsako ir į kitus
  klausimus apie Codeart.
- **Kam video:** programuotojui, kuris naudoja ChatGPT, bet dar nėra
  kūręs savo LLM programos.
- **Ką žiūrovas išsineša:** gali paaiškinti, ką modelis iš tikrųjų gauna,
  iš kur ima atsakymus, kodėl jam reikia tokenų „pagalvoti“, kodėl
  kiekviena žinutė kainuoja vis daugiau ir pagal ką rinktis modelį.
- **2026 m. žvilgsnis.** Kalbame apie tai, kaip yra dabar, o ne prieš
  dvejus metus. 2026 m. tai, ką daro šis video, vadinama **context
  engineering**: sprendimas, ką modelis mato. Kas pasikeitė ir kaip tai
  sakome, surašyta skyriuje „2026 kontekstas“.
- **Ilgis:** apie 16–17 min.
- **Vaizdas:** apie 70 % tikras ekranas, apie 30 % grafika. Kiekvienai
  daliai nurodyta, kas kur.
- **Principas:** kiekviena sąvoka atsiranda kaip klausimas, kurį sau
  užduodu kurdama botą. Tada paaiškinimas, tada įrodymas ekrane. Video
  nesakome nieko, ko negalime parodyti arba pagrįsti šaltiniu.

## Pavadinimas

**Pasirinkta (2026-11-20): How LLMs Actually Work (Before You Build an AI
Chatbot).** Dvi frazės, kurių ieško, ir tiksliai tai, kas yra video.

### Kodėl šis (paieškos duomenys, 2026-11-20)

Google Trends, YouTube paieška, visas pasaulis, 12 mėnesių (santykinis
vidurkis):

| Žodis | Vidurkis | Kas jo ieško |
| --- | --- | --- |
| ai agent | 58 (auga, dabar 94) | Populiariausias, bet mes kuriame ne agentą (agentai yra 3 modulis) |
| ai assistant | 20 | Daugiausia vartotojai: Meta AI, Equal AI skambučių asistentas ir pan. |
| ai chatbot | 9 | Irgi daugiausia vartotojai: Burger King AI chatbot, Claude AI chatbot |
| llm explained | 1 | Labai mažai |

YouTube automatinis papildymas (ką žmonės iš tikrųjų įveda), kai
ieškoma kaip programuotojui:

- **how llms work** → for beginners, explained, simple, visually, internally
- **how chatgpt works** → technically, explained, for beginners, explained simply
- **how to build ai chatbot** → for website, with custom knowledge base,
  for free, from scratch, using google gemini ai, using python
- **llm tokens** → explained, and context window explained
- **gemini api** → tutorial, free, free tier, pricing; *chatbot python gemini*
- **how ai assistants work** → beveik nieko (tik asmeniniai variantai)

Išvados: pavieniai „AI assistant“ ir „AI chatbot“ yra daugiausia
vartotojų paieškos, o programuotojai ieško frazėmis. Savo produktą video
vadiname **AI chatbot**. „Agent“ pavadinime būtų netiesa.

Aprašymui ir žymoms: *llm tokens and context window explained*, *how to
build ai chatbot for website*, *chatbot with custom knowledge base*,
*context engineering*, *gemini api python tutorial*, *gemini api free tier*.

## 2026 kontekstas: kas pasikeitė ir kaip tai sakome

Patikrinta 2026-11-20. Kur šaltinis yra forumas ar neaiškus, pažymėta
„patikrinti demo“.

| Tema | Kaip buvo įprasta sakyti | Kaip yra 2026 m. | Kaip sakome video |
| --- | --- | --- | --- |
| Pavadinimas | „Prompt engineering“ | Mid-2025 paplito terminas **context engineering** (Karpathy, Anthropic 2025-09). Thoughtworks Radar jį pažymėjo „Adopt“ (2026-04). | „In 2026 this has a name: context engineering.“ (1 ir 8 dalys) |
| Atmintis | „API neturi atminties, istoriją siunti pati“ | Chat Completions vis dar be būsenos. Bet naujesnės API saugo istoriją serveryje: OpenAI Responses (`previous_response_id`, Conversations; Assistants API išjungtas 2026-08-26) ir Gemini Interactions API (`previous_interaction_id`). OpenAI rašo, kad visa ankstesnė grandinė vis tiek apmokestinama kaip input. Gemini atveju forume tai neaišku (patikrinti). | „Some newer APIs resend the history for you. But the model still rereads all of it, every message.“ (5 dalis) |
| Kaina už pasikartojantį kontekstą | „Kiekviena žinutė kainuoja vis daugiau“ | Gemini 2.5 ir naujesni modeliai turi **implicit caching** pagal nutylėjimą: pasikartojanti prompto pradžia pigesnė. 3.8 Flash: cached input $0.075, įprastas $0.75 už 1M (10 kartų pigiau). Minimalus dydis 1 024–4 096 tokenų pagal modelį. | Tokenų tiek pat, bet didelė dalis pigesni, jei pastovus turinys (svetainė) eina pradžioje. Mūsų struktūra jau tokia. (6 dalis) |
| Išsigalvojimas iš atminties | „Modeliai išsigalvoja faktus“ | Modeliai dažniau prisipažįsta nežinantys, bet problema išlieka: 2026 Stanford AI Index (AA-Omniscience) rodo 22–94 % haliucinacijų lygį 26 pažangiausiems modeliams, kai jie atsako iš atminties. | „It may now say ‘I don't know’, which is progress. But it still can't know your prices.“ (4.2) |
| Išsigalvojimas su kontekstu | „Su kontekstu problema išspręsta“ | Gerokai mažiau, bet ne nulis: Vectara leaderboard'e modeliai, apibendrindami pateiktą dokumentą, prideda nepagrįstos informacijos 1,8–24,2 % atvejų. | „Much better, not perfect. That's why we'll write tests.“ (4.3) |
| Ilgas kontekstas | „1M tokenų langas: dėk viską“ | **Context rot** (Chroma, 2025-07): modeliai ilgėjant įvesčiai tampa mažiau patikimi net paprastose užduotyse, ypač kai yra panašios, bet netinkamos informacijos. | Visa svetainė (dešimtys tūkstančių tokenų) dar tinka, bet „daugiau“ nėra nemokama. (4.3, 7) |
| Temperature | „Nustatyk temperature 0, kad atsakymai būtų pastovūs“ | Gemini 3 dokumentacija primygtinai rekomenduoja palikti **1.0**: mažesnė gali sukelti kartojimąsi ir prastesnius rezultatus. | Pastovumą duoda kontekstas ir struktūra, ne temperature. (4.1) |
| Mąstymas | „Reasoning modeliai yra atskira rūšis“ | Mąstymas tapo norma: Gemini 3 modeliai mąsto pagal nutylėjimą, kiekį valdo `thinking_level` (per OpenAI-compatible adresą `reasoning_effort`). Mąstymo tokenai apmokestinami kaip output. | Kaip 4.4 dalyje. |
| Aritmetika | „Modeliai nemoka skaičiuoti“ | Mąstantys modeliai paprastus skaičiavimus atlieka gerai, Gemini turi ir kodo vykdymo įrankį. | Kainą skaičiuoja kodas ne todėl, kad modelis nemoka sudėti, o todėl, kad verslo taisyklės turi būti tikslios, pasikartojančios ir patikrinamos. (4.5) |
| Duomenų pateikimas | „Arba visas tekstas prompte, arba RAG nuo nulio“ | Atsirado paprastesnių kelių: Gemini **URL context** įrankis pats perskaito iki 20 URL per užklausą (apmokestinama kaip input tokenai). Gemini **File Search** (2025-11) yra valdomas RAG: saugojimas ir užklausų embeddings nemokami, mokama už indeksavimą. | Trumpai 7 dalyje: mūsų 39 puslapiai viršija 20 URL ribą, o kiekviena užklausa skaitytų iš naujo. Mažai svetainei paprasčiausia paruoštas failas + caching. Kai turinys augs, valdomas RAG. RAG nuo nulio darysime vis tiek, nes reikia suprasti ir to klausia darbdaviai. |

## Eiga

Kiekviena dalis prasideda grafikos kortele su breadcrumb piliule
(„LLM Basics / 01“ … „/ 05“) ir sakiniu „First, …“, „Second, …“.

### 0. Intro: ką sužinosi ir koks rezultatas (0:00–0:30)

Pavadinimas jau pažada, apie ką video. Todėl intro nieko „nekabina“, o
patvirtina, kad žiūrovas gaus būtent tai: išvardija temas, parodo, kaip
jos susijungia į vieną rezultatą, ir tada einame žingsnis po žingsnio.

| Laikas | Ekranas | VO |
| --- | --- | --- |
| 0–5 s | Veikiantis botas (tikras ekranas): lankytojas aprašo projektą, botas klausia patikslinimų ir pateikia preliminarią kainą. | „This is a chatbot I built for my web studio's website. It asks about your project and gives you a rough price.“ |
| 5–22 s | Penki dalykai, kiekvienam 2–3 s tikro kadro su breadcrumb kortele: (1) API kvietimas terminale; (2) žinučių sąrašas su visa svetaine ir tokenų skaičiumi [X]; (3) `reasoning_tokens` išvestis; (4) `usage`, augantis su kiekviena žinute; (5) modelių palyginimo lentelė. | „To understand how it works, you need five things: what the API gives you, what the model actually receives, where its answers come from and why it needs tokens to think, why every message costs more, and how to choose a model.“ |
| 22–30 s | Penkios kortelės susijungia į vieną schemą, kuri virsta veikiančiu botu. | „Put together, that's this chatbot. Let's take it apart, step by step.“ |

- Vaizdas: apie 75 % tikras ekranas, grafika kortelėms ir sujungimui.
- Reikia veikiančio boto, todėl intro filmuojamas paskutinis.
- „Rentgeno“ idėja (viena eilutė lankytojui ir [X] tokenų modeliui,
  AI Studio skaitiklis) persikelia į 3 dalį kaip jos pagrindinis vaizdas.

### 1. The project (0:30–1:30)

- „I'm learning AI engineering, and I learn best on a real project. I run
  a small web studio called Codeart, so I'm building a chatbot for its
  website.“
- Kodėl būtent kaina: užsakovams pirmiausia rūpi, kiek kainuos. Šį
  sakinį sakome tik tada, jei taip yra tavo patirtyje.
- Ką botas darys:
  1. išsiaiškina poreikį (kokios sistemos reikia, kiek vartotojų, kokios
     funkcijos ir integracijos, kada reikia);
  2. pasiūlo tinkamą paslaugą;
  3. pateikia preliminarią kainą („nuo X €“ arba intervalas pagal
     svetainę) ir terminą;
  4. parodo panašų darbą ar straipsnį;
  5. vėliau: užklausa ateina man el. paštu.
  
  Atsako ir į kitus klausimus apie Codeart.
- Dvi taisyklės: kalba tik apie Codeart; kaina visada preliminari.
- Perėjimas: „In 2026 the skill behind this has a name: context
  engineering, deciding what the model sees. To build it, I had to
  understand five things. First, what the API actually gives you. Second,
  what the model actually receives. Third, where its answers come from.
  Fourth, how it remembers a conversation. And fifth, what all of it
  costs.“
- **Ekranas:** codeart.lt paslaugos su „nuo X €“, straipsnis su kainų
  lentele.
- **Grafika:** boto eiga srauto plytelėmis (Questions → Service → Price →
  Timeline → Brief); penkių dalykų sąrašas su varnelėmis.
- Santykis apie 70/30.

### 2. First: what the API gives you (1:30–3:30)

Klausimas: *ką gaunu prijungusi Gemini API? Ar tai jau asistentas?*

- API duoda instruct modelį. Jis jau elgiasi kaip asistentas apskritai:
  atsako, vykdo instrukcijas. Bet jis bendras, ne tavo:
  - nežino, koks jo darbas tavo programoje;
  - nieko nežino apie Codeart;
  - pats nieko neprisimena tarp kvietimų;
  - neturi įrankių (paieškos, el. pašto), kol jų neprijungi.
  
  Visa tai prideda programa aplink jį.
- Trys sluoksniai:
  1. bazinis modelis: tik tęsia tekstą;
  2. instruct modelis: post-training jį paverčia asistentu (šį sluoksnį
     duoda API);
  3. programa: system promptas, duomenys, istorija, įrankiai.
  
  ChatGPT ir Gemini programos irgi yra 3 sluoksnis, tik Google ir OpenAI
  sukurtas.
- Palyginimas: protingas naujas darbuotojas pirmą dieną. Moka kalbą ir
  bendrus dalykus, bet nieko nežino apie tavo įmonę ir po kiekvieno
  pokalbio viską pamiršta. Todėl kiekvieną kartą jam paduodi pareigų
  aprašą ir visą bylą.
- Išvada: „We're not building a model. We're building an application
  around one.“
- **Ekranas:** ChatGPT ar Gemini programa (atmintis, paieška, failai)
  šalia terminalo su API kvietimu, kuris grąžina tik tekstą.
- **Grafika:** trijų sluoksnių schema; darbuotojo kortelė „knows /
  doesn't know“.
- Santykis apie 60/40.

### 3. Second: what the model actually receives (3:30–6:30)

Klausimas: *kaip perduoti svetainės tekstą? Gal tiesiog atskira rolė
„data“?*

- Žinučių sąrašas: `system`, `user`, `assistant`.
- Yra du standartų lygiai:
  1. **API formatas (JSON).** OpenAI Chat Completions formatas tapo de
     facto standartu, kurį kopijuoja kiti: Gemini, Groq, Mistral,
     OpenRouter, Ollama, vLLM turi OpenAI-compatible adresą. Todėl
     naudoju `openai` SDK su Gemini, o tiekėją keičiu vienu `base_url`.
     Savos (native) API skiriasi: Gemini turi `contents` ir `parts`, rolę
     `model` ir atskirą `system_instruction`; Anthropic instrukcijas laiko
     atskirame `system` parametre. 2026 m. ir patys tiekėjai turi
     naujesnes API (OpenAI Responses, Gemini Interactions), bet
     suderinamumo standartas vis dar yra Chat Completions.
  2. **Chat template (tokenai).** Serveris JSON paverčia vienu tekstu su
     specialiais tokenais. Kiekviena modelių šeima turi savo formatą:
     Qwen naudoja ChatML (`<|im_start|>`), Llama 3 naudoja
     `<|start_header_id|>`, o Gemma `<start_of_turn>` su role `model` ir
     be atskiros system rolės. Modelis tik tęsia tekstą po paskutinės
     `assistant` žymos.
- Todėl rolės yra ne laisvai sugalvojami raktai: modelis jas matė
  apmokymo metu. **Demo D2 (patikrinta 2026-11-22):** `"role": "data"` →
  `400 "Invalid role: data"`.
- Papildomas tikras įrodymas, kad JSON tik „vokas“: jei siunčiame vien
  `system` žinutę, Gemini grąžina `400 "contents is not specified"`.
  Suderinamumo sluoksnis `system` perkelia į Gemini `system_instruction`,
  o pačiam pokalbiui reikia bent vienos `user` žinutės.
- Gemini OpenAI compatibility dokumentacijoje leidžiamų rolių sąrašo nėra
  (puslapis pažymėtas kaip beta), todėl video remiamės savo bandymu, ne
  dokumentacija.
- Kur tada dedame duomenis: į `system` turinį tarp žymų
  `<codeart_svetaine>`. Tokenais tampa tik turinys, ne JSON „vokas“.
- **Pagrindinis vaizdas („rentgenas“):** du AI Studio langai su tuo
  pačiu klausimu; dešinysis „atsidaro“, slenka visa svetainė, tokenų
  skaitiklis kyla iki [X]. „The visitor typed one line. The model
  received [X] tokens.“
- **Ekranas:** kodas su žinučių sąrašu; Gemini OpenAI compatibility
  dokumentacija; tikras Hugging Face modelio chat template failas
  (`tokenizer_config.json` arba `chat_template.jinja`) ir mūsų pokalbis,
  paverstas tuo formatu (demo D10); terminalas su klaida.
- **Grafika:** JSON „išsipakuoja“ į chat template, o šis į tokenus.
- Santykis apie 75/25.
- Vėliau verta atskiro video: API formatai ir chat templates išsamiau.

### 4. Third: where the answers come from (6:30–10:00)

Klausimas: *iš kur modelis žino Codeart kainas? Ir kaip jis tą kainą
„apskaičiuoja“?*

**4.1 Kaip gimsta atsakymas.** Modelis kuria atsakymą po vieną tokeną.
Kiekvienam žingsniui jis apskaičiuoja visų galimų kitų tokenų
tikimybes, vienas parenkamas (sampling), prijungiamas prie teksto, ir
viskas kartojasi. Todėl į tą patį klausimą galima gauti skirtingai
suformuluotus atsakymus. **Demo D7:** tas pats klausimas du kartus.
- 2026 pastaba: senesniuose tutorialuose patariama nustatyti
  `temperature` 0, kad atsakymai būtų pastovūs. Gemini 3 dokumentacija
  primygtinai rekomenduoja palikti 1.0, nes mažesnė reikšmė gali sukelti
  kartojimąsi ir prastesnius rezultatus. Pastovumą duoda kontekstas ir
  struktūra.

**4.2 Iš atminties (parametric knowledge).** 2026 m. modeliai dažniau
prisipažįsta nežinantys, ir tai pažanga. Bet iš atminties jie vis dar
dažnai klysta: 2026 Stanford AI Index (AA-Omniscience testas) rodo 22–94 %
haliucinacijų lygį 26 pažangiausiems modeliams. O Codeart kainų jie
negali žinoti iš principo. **Demo D3a.**

**4.3 Su kontekstu (grounding).** Procesas tas pats, bet tikėtiniausias
tęsinys dabar remiasi tekstu prompte. Atsakymas atitinka svetainę, ir jį
galima patikrinti pagal šaltinį. Bet ne 100 %:
- net apibendrindami pateiktą dokumentą modeliai kartais prideda
  nepagrįstos informacijos (Vectara leaderboard: 1,8–24,2 %);
- ilgėjant įvesčiai jie tampa mažiau patikimi (context rot, Chroma 2025).

Todėl vėliau rašysime testus (4 modulis). **Demo D3b.**
- Tikras momentas iš darbo: pirmoji teksto ištraukimo versija praleido
  visus DUK klausimus. Pastebėjau tik patikrinusi failą. Pamoka: visada
  pažiūrėk, kas iš tikrųjų patenka į promptą.
- Tas pats principas paaiškina, kaip ChatGPT „perskaito“ vakar išėjusį
  straipsnį: paieška → tekstas į kontekstą → atsakymas. Modelis to
  straipsnio neišmoksta.

**4.4 Modeliui reikia tokenų „pagalvoti“.** Kiekvienam tokenui modelis
atlieka ribotą skaičiavimo kiekį. Užduoties iš kelių žingsnių (pvz.,
sujungti kelias paslaugas į vieną kainą) vienu tokenu neišspręsi:
modeliui reikia išrašyti tarpinius žingsnius. 2026 m. tai tapo norma:
dauguma modelių prieš atsakymą patys sugeneruoja paslėptus mąstymo
tokenus.
- Gemini 3 modeliai mąsto pagal nutylėjimą. Kiekį valdo
  `thinking_level`, per OpenAI-compatible adresą `reasoning_effort`.
- Mąstymo tokenai apmokestinami kaip output ir matosi `usage` lauke kaip
  `reasoning_tokens`.
- Daugiau mąstymo duoda geresnius atsakymus į sudėtingus klausimus, bet
  atsakymas lėtesnis ir brangesnis.
- **Demo D6:** tas pats kainos klausimas su `low` ir `high`: atsakymas
  ir `reasoning_tokens`.

**4.5 Kas skaičiuoja kainą.** Mąstantys modeliai paprastą aritmetiką
2026 m. atlieka gerai, o Gemini turi ir kodo vykdymo įrankį. Vis tiek
galutinę kainą verta skaičiuoti kode: modelis surenka duomenis, Python
suskaičiuoja (3 tutorialas, structured output). Ne todėl, kad modelis
nemoka sudėti, o todėl, kad verslo taisyklės turi būti tikslios,
kiekvieną kartą vienodos ir patikrinamos.

- **Ekranas:** terminalas (D3, D6, D7), `codeart.md` VS Code'e,
  ChatGPT ar Gemini atsakymas su šaltinių nuorodomis, Gemini 3
  dokumentacijos pastraipa apie temperature.
- **Grafika:** kito tokeno tikimybių stulpeliai; dvi kortelės
  „iš atminties / su kontekstu“; mąstymo tokenai kaip pilkos juostelės
  prieš mint spalvos atsakymą.
- Santykis apie 65/35.
- Mokymuisi: Karpathy „Deep Dive into LLMs like ChatGPT“ dalys apie
  tokenizaciją ir apie tai, kad modeliams reikia tokenų mąstyti; Gemini
  dokumentacija apie thinking; Chroma „Context Rot“.

### 5. Fourth: how it remembers (10:00–11:30)

Klausimas: *kaip botas prisimins, ką lankytojas sakė prieš tai?*

- Modelis pats nieko neprisimena. Kiekvieną kartą jis iš naujo perskaito
  visą pokalbį.
- Klasikinė Chat Completions API neturi būsenos: istoriją siunčiame mes.
  Mūsų atveju kartu kiekvieną kartą siunčiama ir visa svetainė.
- Tikri skaičiai: istorija prideda tik ~50 tokenų per ėjimą, o kainą
  lemia svetainė (~62 000 tokenų), siunčiama kiekvieną kartą. Net „ok“
  kainavo 62 035 input tokenus, iš jų 96 % paėmė cache. Video sakome
  būtent tai, ne „istorija brangina“.
- 2026 m. kai kurios naujesnės API (OpenAI Responses, Gemini
  Interactions) saugo istoriją serveryje, ir siųsti jos nereikia. Bet
  modelis vis tiek ją visą perskaito iš naujo, ir OpenAI tie tokenai vis
  tiek apmokestinami kaip input. Patogiau, bet ne pigiau.
- Kaip tai valdyti (tik paminime, bus atskiri video): riboti arba
  apibendrinti istoriją, caching (pastovus turinys pradžioje), RAG.
- **Ekranas:** terminale auga žinučių sąrašas, po kiekvieno ėjimo
  rodomas `usage` (demo D5); žinutė „ok“ ir jos tokenų skaičius (D9).
- **Grafika:** žinučių krūvelė, kurią modelis kaskart perskaito visą.
- Santykis apie 65/35.

### 6. Fifth: what it costs (11:30–13:00)

Klausimas: *kiek man kainuos vienas klausimas?*

- Kas yra tokenas: trumpai ir vizualiai. Pažymime, kad kiekvienas
  modelis tekstą skaido savaip.
- `usage` laukas: input, output, reasoning, cached tokenai. **Demo D1.**
- Kiek tokenų užima visa svetainė. **Demo D4.**
- Lietuviška ir angliška tos pačios svetainės dalis: kiek tokenų užima
  kiekviena. **Demo D8.** Sakome tik tai, ką parodys skaičiai. Jei
  lietuviškas tekstas užims daugiau, tai paaiškina, kodėl instrukcijas
  rašome angliškai, o atsakymas būna lankytojo kalba.
- Formulė: **kaina = tokenų skaičius × tokeno kaina**.
  - Daugiau konteksto ir mąstymo reiškia daugiau tokenų.
  - Didesnis modelis reiškia brangesnį tokeną.
  - 2026: implicit caching. Jei pastovus turinys (instrukcijos ir
    svetainė) eina pradžioje, jo pasikartojantys tokenai kainuoja
    gerokai pigiau (3.8 Flash: 10 kartų). Tokenų skaičius tas pats,
    sąskaita mažesnė.
- **Ekranas:** terminalas, Gemini kainų puslapis, AI Studio.
- **Grafika:** kainos formulė; prompto juosta, kurioje pastovi pradžia
  pažymėta kaip „cached“.
- Santykis apie 70/30.

### 7. Which model should I use? (13:00–15:45)

Čia sujungiame viską, kas buvo.

- Kuo modeliai skiriasi: duomenys ir žinių riba, dydis, „charakteris“ iš
  post-training, kalbos, filtrai, kaina, limitai, duomenų politika.
- Nė vienas modelis nėra patikimas faktų šaltinis. Kadangi faktus duodame
  mes, renkamės ne pagal tai, kuris daugiau žino, o pagal kriterijus:
  - gerai rašo lietuviškai;
  - neišsigalvoja to, ko nėra tekste;
  - laikosi taisyklių per visą pokalbį;
  - susitvarko su ilgu kontekstu (visa svetainė);
  - pakankamai „pagalvoja“, kai reikia sudėtingesnės kainos;
  - kaina ir greitis.
- **Ar apsimoka naujesnis modelis? (apie 1 min, demo D11).** Mažas
  testų rinkinys (5–8 klausimai) paleidžiamas per tris Gemini modelius:
  senesnį pigų (pvz., 3.5 Flash-Lite), vidurinį (3.6 Flash) ir naujausią
  (3.8 Flash). Klausimai tikrina mūsų kriterijus: kainos klausimas,
  sudėtingesnė kaina iš kelių paslaugų, atsakymas lietuviškai, klausimas,
  kurio atsakymo svetainėje nėra, bandymas išvesti iš temos.
  - Lentelė ekrane: ar atsakė teisingai, ar laikėsi taisyklių, tokenai,
    kaina už pokalbį, atsakymo laikas.
  - Išvadą sakome pagal rezultatus, ne iš anksto: ar naujesnio modelio
    kokybė verta jo kainos mūsų užduočiai.
  - Platesnis palyginimas (kiti tiekėjai, daugiau modelių) bus atskirame
    video.
- Ar negalima paprasčiau? 2026 m. Gemini gali pats perskaityti puslapius
  (URL context, iki 20 URL) arba naudoti valdomą RAG (File Search). Mūsų
  39 puslapiai viršija URL ribą, ir kiekviena užklausa juos skaitytų iš
  naujo. Mažai svetainei paprasčiausia paruoštas failas ir caching. Kai
  turinio daugės, rinksimės RAG.
- Kol kas naudoju Gemini nemokamą lygį. Pastaba: nemokamame lygyje
  Google naudoja užklausas, todėl siunčiu tik viešą svetainės tekstą.
- **Ekranas:** Gemini modelių ir kainų puslapis, AI Studio limitai,
  URL context ir File Search dokumentacija.
- **Ekranas (D11):** testų paleidimas terminale ir rezultatų lentelė.
- **Grafika:** kriterijų sąrašas su varnelėmis.
- Santykis apie 65/35.

### 8. Recap and next (15:45–16:45)

- Penki dalykai vienoje schemoje: API → žinutės → atsakymų šaltinis →
  atmintis → kaina. Visa tai kartu yra context engineering.
- Kitame video rašome kodą: pirmas kvietimas, pokalbio ciklas, tokenai
  kiekvienoje žinutėje.
- Kodas GitHub'e, nuoroda aprašyme.
- **Ekranas:** veikiantis botas terminale (jei jau bus). **Grafika:**
  santraukos schema.

Bendras santykis pagal šias dalis yra apie 2/3 tikro ekrano. Iki 70 %
galima priartėti santraukoje rodant veikiantį botą.

## Filmavimo taisyklės

- **Kalba.** Video angliškas, todėl demo klausimai ir kodas ekrane
  angliškai (pvz., „How much would a booking system cost?“). Botas atsako
  lankytojo kalba, todėl atsakymai irgi bus angliški.
- **Viena lietuviška vieta.** Rodome vieną pokalbį lietuviškai su angliška
  antrašte ekrane: tai įrodo taisyklę „reply in the user's language“ ir
  tinka D8 (lietuviškas tekstas užima daugiau tokenų).
- **Skaičiai iš to paties įrašo.** Kiekvienas paleidimas duoda kitą
  atsakymą ir kitus tokenus, todėl VO skaičiai imami iš to kadro, kuris
  rodomas video, o ne iš ankstesnių bandymų.
- **Klaidos tekstas matomas.** SDK rodo tik `Error code: 400`. Kad
  žiūrovas matytų priežastį (`Invalid role: data`), demo metu
  atspausdiname klaidos turinį (`e.response.text`).
- **Neatkartojami momentai.** Kai kurių dalykų vėliau gali nepavykti
  pakartoti (pvz., 3.8 Flash perkrova ir 503). Jei tokių momentų norime
  video, filmuojame juos iškart, kai pasitaiko.

## Demo, kurias reikia nufilmuoti

Visoms reikia veikiančio 1 dalies kodo (D5 reikia ir 2 dalies), todėl
filmuoti verta po jo.

| Nr. | Kas | Kur video |
| --- | --- | --- |
| D1 | Pirmas kvietimas ir `usage` išvestis | 6 |
| D2 | `"role": "data"` → klaida | 3 |
| D3 | Tas pats kainos klausimas be svetainės teksto (a) ir su juo (b). Hook'ui filmuojama Google AI Studio, kad matytųsi tokenų skaitiklis. | hook, 4 |
| D4 | Kiek tokenų užima visa svetainė | hook, 6 |
| D5 | Input tokenų augimas per kelias žinutes | 5 |
| D6 | Tas pats kainos klausimas su `reasoning_effort` `low` ir `high` | 4 |
| D7 | Tas pats klausimas du kartus, skirtingi atsakymai | 4 |
| D8 | Lietuviškos ir angliškos svetainės dalies tokenų skaičius | 6 |
| D9 | Žinutė „ok“ po kelių ėjimų ir jos `usage` (su `cached_tokens`, jei bus) | 5, 6 |
| D10 | Mūsų pokalbis, paverstas atviro modelio (pvz., Qwen) chat template formatu (`apply_chat_template`) | 3 |
| D11 | 5–8 testinių klausimų per 3 Gemini modelius: teisingumas, taisyklės, tokenai, kaina, laikas | intro, 7 |
| D12 | Veikiantis botas: lankytojas aprašo projektą, gauna preliminarią kainą | intro, 8 |

## Tikri skaičiai iš paleidimų

| Data | Ką matavome | Rezultatas |
| --- | --- | --- |
| 2026-11-20 | Visa svetainė (D4) | 61 647 input tokenų; su instrukcijomis 61 826 |
| 2026-11-20 | `gemini-3.8-flash`, nemokamas lygis | Mažas klausimas: klaida 503 (serveris perkrautas) po 58 s; su visa svetaine neatsakė per 90 s |
| 2026-11-20 | `gemini-3.5-flash-lite` | Atsakė per 3,5–4,1 s; kainos ir terminai teisingi pagal svetainę; viena lietuviška klaida („Tikslikė“) |
| 2026-11-20 | `usage` per OpenAI-compatible adresą (3.5 Flash-Lite) | `completion_tokens_details` yra `None`: `reasoning_tokens` šiam modeliui negrąžinami |
| 2026-11-22 | Tas pats klausimas antrą kartą (D7) | Kitas atsakymas: kitokia struktūra, 432 output tokenai vietoj 311; faktai tie patys |
| 2026-11-22 | `"role": "data"` (D2) | `400 INVALID_ARGUMENT: "Invalid role: data"`. Tas pats su sugalvota role `banana`. (Pirmas bandymas atrodė be klaidos, nes `main.py` pakeitimas nebuvo išsaugotas.) |
| 2026-11-22 | 5 ėjimų pokalbis EN (D5, D9) | Input 61 877 → 62 092: istorija prideda tik ~50 tokenų per ėjimą. „ok“ = 62 035 input tokenų. Nuo 2 ėjimo cached ~59 330 (96 %). Atsakymas 1,1–1,6 s |
| 2026-11-22 | LT ir EN svetainės dalis (D8) | LT 18 511 tokenų (2,46 / žodį), EN 11 968 (1,38 / žodį): lietuviškai ~55 % daugiau tokenų |
| 2026-11-22 | Atmintis ir užmarštis | Su istorija vardą prisiminė, be istorijos ne |
| 2026-11-22 | Cache nepataikė (LT pokalbis) | `cached 0`, atsakymas 9,5–9,8 s vietoj 1–2 s: cache veikia ir greitį |
| 2026-11-22 | Mąstymo tokenai per OpenAI-compatible adresą (D6) | 3.6 Flash ir 3.8 Flash su `low` / `high`: `reasoning_tokens` negrąžinamas (`None`), output tik 46–55 tokenai, bet laikas 33–83 s, o 3.8 `high` neatsakė per 90 s. Mąstymas vyksta, bet per šį adresą jo nematyti. D6 filmuoti per Gemini savą SDK (`google-genai`, `thoughts_token_count`) arba AI Studio |
| 2026-11-22 | Rasti trūkumai | Į angliškai parašytą „Hi, my name is Gabriele“ atsakė lietuviškai (kalbos taisyklė pažeista); kainos nenuoseklios („nuo 500 €“, paskui „nuo 1 000 €“; LT išgalvota „nuo 1 500 €“); 3 ėjime vietoj preliminarios kainos pasiūlė rašyti el. paštu |
| 2026-11-22 | Tik `system` žinutė, be `user` | `400: "GenerateContentRequest.contents: contents is not specified"`. Įrodo, kad Gemini suderinamumo sluoksnis `system` perkelia į atskirą `system_instruction`, o pokalbiui reikia bent vienos `user` žinutės |
| 2026-11-22 | Implicit caching (D9) | Trečią paleidimą iš eilės `cached_tokens=59357` iš 61 826 input (96 %). Pirmus du kartus `prompt_tokens_details` buvo `None`, t. y. cache nepataikė |

## Ką patikrinti per demo, kad video nemeluotų

- Ar AI Studio rodo tokenų skaičių taip, kad jį galima nufilmuoti
  (hook'ui).
- Ką modelis be konteksto atsako į kainos klausimą: išsigalvoja ar
  prisipažįsta nežinantis (nuo to priklauso hook'o VO ir atsarginis
  variantas).
- Ar `gemini-3.8-flash` per OpenAI-compatible adresą priima
  `reasoning_effort` ir kokias reikšmes. Forume pranešta, kad Gemini 3
  Flash atveju reikšmė `minimal` per šį adresą buvo atmesta.
- `usage` per OpenAI-compatible adresą (patikrinta 2026-11-22):
  `cached_tokens` grąžina, `reasoning_tokens` ne. D6 reikia Gemini savo
  SDK arba AI Studio. Kol to nepatikrinsime, video nesakome konkretaus
  mąstymo tokenų skaičiaus.
- `"role": "data"`: patikrinta 2026-11-22, Gemini grąžina 400
  „Invalid role: data“. Filmuojant D2 įsitikinti, kad pakeitimas
  išsaugotas.
- Ar lietuviškas tekstas tikrai užima daugiau tokenų (D8).
- Gemini Interactions API: ar serveryje saugoma istorija apmokestinama
  (forume klausimas be atsakymo). Jei nepavyks išsiaiškinti, video
  sakome tik apie OpenAI, kur tai parašyta dokumentacijoje.
- Gemini vidinis chat template nėra viešas. Todėl D10 rodome atvirą
  modelį ir video tai pasakome.
- D11 modelių pavadinimai ir kainos: ar 3.5 Flash-Lite ir 3.6 Flash dar
  prieinami, kiek kainuoja 3.6 Flash ir koks jų nemokamo lygio limitas.
- **Kainos prieš paskelbiant.** 3.8 Flash kaina ($0.75 / $3.75 už 1M)
  galioja iki 2026-12-31, paskui dvigubėja. Jei video išeis vėliau,
  skaičius atnaujinti.

## Grafika (Warm Technical)

Breadcrumb kortelė kiekvienai daliai; tokenų skaitiklio padidinimas
hook'e; boto eiga; penkių dalykų sąrašas; trys sluoksniai; darbuotojo
kortelė; JSON → chat template → tokenai; tikimybių stulpeliai; atmintis
ir kontekstas; mąstymo tokenai; auganti istorija; prompto juosta su
cached dalimi; kainos formulė; kriterijų sąrašas; santrauka.

## Shorts kandidatai

- „Why there's no `data` role in the ChatGPT API“ (3 dalis, D2).
- „Stop setting temperature to 0 on Gemini 3“ (4.1, šaltinis: Gemini 3
  dokumentacija).
- „Your chatbot rereads the whole conversation every message“ (5 dalis,
  D9).
- „LLMs need tokens to think“ (4.4, D6).

## Kas nepateko (kitiems video)

- API formatai ir chat templates išsamiau → atskiras video.
- Valdomas RAG (Gemini File Search, OpenAI file_search) ir RAG nuo nulio:
  kada kuris → RAG modulio įžanga.
- Atviri modeliai savo serveriuose, vidinis įmonės asistentas → 20
  tutorialas (Ollama) arba atskiras video.
- Paieška internete kaip įrankis → 3 modulis (tool calling).
- Kodėl modeliai vis dar apmokomi, fine-tuning ar RAG → RAG modulio
  įžanga.
- Nemokamų API palyginimas → atskiras video.
- Visas kontekstas ar RAG: tokenai ir kaina → atskiras video.
- Darbo rinka ir AI klaidos programuojant → ne šio kanalo tema.

## Atviri sprendimai

1. Intro skaičius ([X] tokenų ir kt.) įrašyti po demo.
2. Ar tai atskiras video (1 dalis: sąvokos), o kodas eina į 2 dalį?
   Siūlymas: atskiras, nes vien sąvokos užima apie 15 min.
3. Kada filmuoti? Siūlymas: po 1 dalies kodo, kad demo ir skaičiai būtų
   tikri.
4. Veidas kameroje ar tik balsas ir ekranas?
5. Šriftas ir įrankis 16:9 grafikai (žr. stiliaus failo atvirus
   klausimus).

## Šaltiniai (2026-11-20)

- Context engineering: [Thoughtworks Radar](https://www.thoughtworks.com/radar/techniques/context-engineering)
- Atmintis: [OpenAI Assistants → Responses migracija](https://developers.openai.com/api/docs/assistants/migration),
  [forumas apie `previous_response_id` apmokestinimą](https://community.openai.com/t/responses-api-question-about-managing-conversation-state-with-previous-response-id/1141633),
  [Gemini Interactions API](https://ai.google.dev/api/interactions-api),
  [forumas apie Interactions istorijos apmokestinimą](https://discuss.ai.google.dev/t/interactions-api-is-the-stored-history-of-previous-interaction-id-billed-and-why-is-it-missing-from-usage/187450)
- Caching: [Gemini context caching](https://ai.google.dev/gemini-api/docs/caching)
- Haliucinacijos: [Stanford AI Index 2026, 3 skyrius](https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_3_responsible_ai.pdf),
  [AA-Omniscience](https://artificialanalysis.ai/articles/aa-omniscience-knowledge-hallucination-benchmark),
  [Vectara leaderboard](https://github.com/vectara/hallucination-leaderboard/)
- Ilgas kontekstas: [Chroma: Context Rot](https://research.trychroma.com/context-rot)
- Temperature ir thinking: [Gemini 3 developer guide](https://ai.google.dev/gemini-api/docs/gemini-3),
  [Gemini OpenAI compatibility](https://ai.google.dev/gemini-api/docs/openai)
- Paprastesni keliai: [URL context](https://ai.google.dev/gemini-api/docs/url-context),
  [File Search](https://ai.google.dev/gemini-api/docs/file-search),
  [File Search pristatymas](https://blog.google/technology/developers/file-search-gemini-api/)
