# AI inžinerijos planas

Sukurta 2026-11-14. Gyvas dokumentas: atnaujink būsenas ir sprendimus čia.

## Tikslas

1. **Išmokti AI inžinerijos** tiek, kad atitikčiau Vilniaus AI Engineer
   skelbimų reikalavimus.
2. **Susirasti AI Engineer / LLM Engineer darbą.**

Kanalas yra priemonė, ne tikslas. Tapti viraliai nesiekiu. Sėkmę matuoju
paskelbtais tutorialais, veikiančiu kodu GitHub'e ir pokalbiais su
darbdaviais, ne peržiūromis.

## Sprendimai

| Kas | Sprendimas |
| --- | --- |
| Platforma | **Tik YouTube**: ilgi tutorialai, o Shorts karpomi iš jų. TikTok ir Instagram nenaudoju. |
| Turinys | Gryni tutorialai ir paaiškinimai. Niša siaura, bet tai gerai: tutorialus žmonės randa per paiešką. |
| Kalba | Video ir LinkedIn angliškai (Vilniaus AI darbdaviai dirba angliškai, YouTube paieška globali). |
| Programavimo kalba | Python (jo prašo beveik visi skelbimai). Frontend'ui, kur reikia, React. |
| LLM tiekėjas | Kol kas **Gemini API, nemokamas lygis**. |
| Kaip dirbu su Claude | Kodą projektuoju ir rašau pati, visi sprendimai mano. Claude paaiškina, pateikia variantus ir peržiūri kodą, bet sprendimo už mane nerašo. |
| LinkedIn | Vienas įrašas po kiekvieno paskelbto tutorialo: ką sukūriau, ką išmokau, nuoroda. |
| GitHub | Kiekvieno tutorialo kodas šiame repo. Vėliau repo bus viešas ir naudojamas kaip portfolio. |
| Darbo tvarka | **Ne kalendorius, o eilė.** Kai turiu laisvo laiko, darau kitą žingsnį. Vienu metu darau tik vieną tutorialą. |
| TikMaker | Lieka baigiamojo darbo projektu ir čia nesimaišo. Jei jame reikės ką keisti, keičiu atskiroje šakoje nuo `main`. |

## Ko prašo darbdaviai

Remiantis Vilniaus skelbimais (Oxylabs, Ignitis, NFQ, Nortal, Andersen,
cvbankas, 2026-11):

- stiprus **Python**;
- **RAG nuo nulio**: duomenų įkėlimas, chunking, embeddings, vektorinė DB, dideli dokumentų rinkiniai;
- framework'ai: **LangChain, LlamaIndex, LangGraph**;
- **evals ir observability**;
- **agentai, MCP**;
- **Docker**, debesis (AWS, GCP, Azure), lokalūs modeliai (Ollama, vLLM).

Todėl RAG modulis yra didžiausias.

## Projektas: Codeart asistentas

Vienas projektas, kuris auga per visus modulius: AI asistentas svetainėje
[codeart.lt](https://codeart.lt).

- **Ką daro:** pagrindinė kryptis yra kaina. Botas išklausinėja lankytoją
  apie jo projektą ir pateikia preliminarią kainą bei terminą, nes
  užsakovams labiausiai rūpi sužinoti kainą. Atsako ir į kitus klausimus
  apie paslaugas, darbo eigą ir atliktus darbus (LT ir EN).
- **Kaina pagal mano valandas (sprendimas 2026-11-20).** Ne tik „nuo X €“
  iš svetainės, o mano kainodara: valandinis įkainis, tipiniai darbai su
  valandomis (min–max), kas didina laiką, pastovios dalys ir atsarga.
  Ją surašau pati į `knowledge/pricing.md`. Modelio neapmokome: kainodara
  pateikiama kaip duomenys, kad ją būtų galima keisti per minutę.
  1–2 tutorialuose kainą skaičiuoja modelis iš lentelės prompte, nuo 3
  tutorialo modelis grąžina reikalingus darbus struktūruotai, o valandas
  ir kainą skaičiuoja Python.
- **Asistentas, ne tik chatbot'as: geras pardavėjas (sprendimas
  2026-11-20).**
  - Siūlo alternatyvas, kai kaina per didelė: MVP, darbą etapais,
    paprastesnį sprendimą, kuris užima mažiau valandų.
  - Nuolaidą siūlo tik pagal mano taisykles (jas dar reikia surašyti).
  - Galutinės kainos nepažada. Vietoj to paruošia preliminarų pasiūlymą
    (darbai, valandos, kaina, terminas), kuris ateina man el. paštu, o
    lankytojui sako, kad patvirtinsiu aš. Priežastis: žinomi atvejai, kai
    įmonė turėjo vykdyti boto pažadą (Air Canada, 2024), ir žmonės bando
    botus įkalbėti.
  - Vėliau įrankiai (3 modulis): kainos skaičiuoklė, laikas skambučiui,
    pasiūlymo išsiuntimas. Testai (4 modulis): niekada nepažada galutinės
    kainos, neduoda nuolaidos už taisyklių ribų, nepasiduoda įkalbinėjimui.
- **Kodėl būtent jis:**
  - pirmiausia tai mokymosi projektas: kuriu jį, kad išmokčiau, o ne todėl,
    kad verslui jo būtinai reikia (video taip ir sakau);
  - svetainė turi tikrų lankytojų;
  - tai gyvas pavyzdys paslaugos, kurią svetainė jau parduoda („AI chatbot ir
    DI sprendimai verslui“);
  - tai portfolio projektas, kurį darbdavys gali išbandyti pats;
  - kiekvienas modulis jam suteikia naują galimybę.
- **Taisyklės nuo pirmos dienos:** jokių galutinių kainų: kaina visada
  preliminari ir taip ir pažymėta, galutinę patvirtinu aš; nuolaidos tik
  pagal mano taisykles; kalba tik apie Codeart; užklausų ir išlaidų
  limitas.
- **Techniškai:** svetainė statinė (GitHub Pages, vanilla JS). Todėl reikės
  atskiro Python backend'o (FastAPI) ir mažo įterpiamo chat widget'o.

| Modulis | Ką gauna asistentas |
| --- | --- |
| 1. LLM pagrindai | Atsako iš viso svetainės teksto prompte; aiškios taisyklės; užklausa kaip struktūruoti duomenys; veikia svetainėje |
| 2. RAG | Ieško straipsniuose, projektų aprašymuose ir paslaugų puslapiuose, o ne kemša viską į promptą |
| 3. Agentai | Įrankiai: laisvas laikas skambučiui, užklausos įrašymas, projekto pavyzdžio paieška; MCP serveris su Codeart turiniu |
| 4. Patikimumas | 30+ tikrų klausimų testų rinkinys: nežada kainų, atsako ta pačia kalba, neišsigalvoja projektų |
| 5. Produkcija | Docker, pokalbio kaina, caching, limitai, stebėjimas |

## Tutorialų eilė

Būsenos: `[ ]` laukia · `[~]` darau · `[x]` paskelbta

### 1. LLM pagrindai
Asistentas atsako iš svetainės teksto ir veikia codeart.lt.
- [~] 1. Pirma LLM programėlė Python'e: API, tokenai, kaina (CLI asistentas su visu svetainės tekstu prompte; kiek kainuoja vienas klausimas)
- [ ] 2. System prompt ir few-shot: tonas, LT/EN, taisyklės (jokių fiksuotų kainų, tik apie Codeart)
- [ ] 3. Structured output su Pydantic: pokalbis virsta projekto užklausa ir ateina el. paštu
- [ ] 4. Streaming chat: FastAPI ir įterpiamas widget'as statinėje svetainėje, pirmas paleidimas

### 2. RAG
Asistentas ieško Codeart turinyje. Dažniausias reikalavimas skelbimuose.
- [ ] 5. Embeddings ir semantinė paieška
- [ ] 6. Vektorinės DB: pgvector, Chroma
- [ ] 7. RAG nuo nulio, be framework'ų
- [ ] 8. Chunking strategijų palyginimas
- [ ] 9. Hybrid search ir reranking
- [ ] 10. RAG su LlamaIndex/LangChain: kada framework'as verta

**Po 10 tutorialo pradedu siųsti CV.** Iki tol jau turiu tai, ko prašo
daugelis skelbimų.

### 3. Agentai
Asistentas gauna įrankius.
- [ ] 11. Tool calling nuo nulio
- [ ] 12. Agento ciklas be framework'ų
- [ ] 13. Savo MCP serveris
- [ ] 14. LangGraph: agentas su būsena

### 4. Patikimumas
Asistento testų rinkinys.
- [ ] 15. RAG evals: kaip išmatuoti atsakymų kokybę
- [ ] 16. LLM-as-judge ir testų rinkinys
- [ ] 17. Tracing ir observability (Langfuse)

### 5. Produkcija
Asistentas paruoštas produkcijai.
- [ ] 18. Docker ir deploy į debesį
- [ ] 19. Kaina ir greitis: caching, modelio pasirinkimas
- [ ] 20. Lokalūs modeliai (Ollama)

### Vėliau
- ML pagrindai, fine-tuning ar RAG, LoRA
- TikMaker kaip atvejo analizė: kaip sukūriau agentų sistemą, kuri kuria
  video (po baigiamojo darbo gynimo)

## Kur sustojome (2026-11-22)

1 tutorialas: 1 ir 2 dalys veikia (`main.py`: pokalbio ciklas su
istorija, tokenai, klaidų gaudymas). Bandymų įrašai `runs/`, tikri
skaičiai `video-plan.md`.

**Kitas mano darbas: užpildyti `code/knowledge/pricing.md`** (visur, kur
`____`):

- **A. Įkainis:** valandinis įkainis (pvz., `40 € per hour`) ir minimali
  projekto kaina, ne mažesnė už svetainės „nuo“ kainas (integracija 500 €,
  chatbot 800 €, aplikacija 1 000 €, verslo sistema 2 500 €).
- **B. Darbai:** kiekvienam darbui Min h (paprasta versija) ir Max h
  (sudėtinga). Nereikalingas eilutes ištrinti, savas pridėti. Svarbiausia
  dalis.
- **C. Kas ilgina darbą:** kelios kalbos, mobilioji programėlė, daug rolių,
  neaiškūs reikalavimai: `+__ %` arba `+__ h`.
- **D. Kas įeina visada:** planavimo, testavimo, paleidimo valandos ir
  atsarga procentais.
- **E. Terminas:** kiek valandų per savaitę skiriu vienam projektui.
- **F. Nuolaidos:** kokią ir kada botas gali siūlyti, arba `none`.
- **G.** Neprivaloma papildoma taisyklė apie tai, kaip botas kalba apie
  kainą.

Skaičiai gali būti apytiksliai: valandos tokios, kokias realiai užtrunku
aš. Vėliau pataisysiu pagal testus.

**Po to:** prijungti `pricing.md` prie prompto → botas-pardavėjas
(klausinėja, skaičiuoja pagal valandas, siūlo alternatyvas) → filmavimo
scenarijus → filmavimas.

## Atviri klausimai

### Gemini nemokamas lygis ir gyva svetainė (nuspręsti prieš 4 tutorialą)
- Nemokamame lygyje Google naudoja užklausas ir atsakymus savo produktams
  tobulinti. Todėl ten siunčiu tik viešą svetainės tekstą, jokių asmens
  duomenų.
- 2025-12-18 Gemini API sąlygų versijoje parašyta: jei programa skirta
  vartotojams EEE (taigi ir Lietuvoje), leidžiamos tik mokamos paslaugos.
  Prieš paleidžiant asistentą codeart.lt, patikrinti dabartines sąlygas ir
  tikriausiai įjungti mokamą lygį su išlaidų limitu.

### Kainodara ir nuolaidos (surašyti prieš 4 žingsnį: botas, kuris klausinėja apie kainą)
- `knowledge/pricing.md`: valandinis įkainis, darbai su valandomis,
  laiką didinantys dalykai, pastovios dalys, atsarga.
- Nuolaidų taisyklės: kada ir kiek (pvz., iki 10 %, jei apmokama iš
  karto).
- Kaina iš valandų neturėtų būti mažesnė už svetainėje skelbiamą „nuo X €“
  (svetainėje: verslo sistemos nuo 2 500 €, aplikacijos nuo 1 000 €,
  integracijos nuo 500 €, chatbot nuo 800 €). Jei taip nutinka, pataisyti
  lentelę arba svetainę.
- Nemokamame Gemini lygyje Google naudoja užklausas, todėl įkainis pateks
  pas juos. Nuspręsti, ar tai priimtina.

### Tutorialo struktūra (nuspręsti vėliau)
Juodraštis, kol kas nepatvirtintas:
- Vieno tutorialo eiga: mokausi → kodas → scenarijus → įrašymas →
  montavimas ir paskelbimas → Shorts ir LinkedIn. Kiekvienas žingsnis apie
  vieną laisvo laiko sėdėjimą.
- Ilgo video šablonas (10–20 min): galutinis rezultatas → sąvoka su schema →
  kūrimas žingsnis po žingsnio → 1–2 dažnos klaidos → santrauka ir kodas.
- Shorts: 2 iš kiekvieno tutorialo (sąvoka per 60 s, viena klaida arba
  patarimas), abu nukreipia į ilgą video.

### Įrankiai video kūrimui
- Ilgą tutorialą sudaro ekrano įrašas ir balsas. Įrašymui tinka OBS
  (nemokamas) arba Screen Studio, montavimui DaVinci Resolve (nemokamas),
  Descript arba CapCut. Įrankius pasirinkti prieš 1 tutorialą.
- **TikMaker formatas 16:9.** Dabar TikMaker daro tik 1080×1920:
  projekto schema leidžia tik šį dydį, apie 35 failai turi įrašytas
  vertikalias koordinates, o agento scenų skill'ai aprašo vertikalią
  „paveikslo zoną“. Galimi du keliai:
  - *A, mažesnis:* 16:9 palaikymas tik kodo scenoms (schemos ir sąvokų
    animacijos ilgam video). Keistųsi kompozicijos dydis pagal projektą,
    schema ir 16:9 paveikslo zona scenų skill'e.
  - *B, pilnas:* formato pasirinkimas visur (senasis renderis, editorius,
    safe zones, šablonai). Gerokai didesnis darbas ir rizika baigiamajam
    darbui.
  - Shorts (9:16) TikMaker gali daryti jau dabar, be pakeitimų.
  - Sprendimas: nuspręsti po 1–2 tutorialų, kai paaiškės, ar schemų dalies
    tikrai reikia iš TikMaker. Jei reikės, daryti A atskiroje šakoje.

## Šio repo struktūra (kai pradėsiu tutorialus)

```
ai-eng-lab/
  PLAN.md            – šis failas
  README.md          – paskelbtų tutorialų sąrašas su nuorodomis (portfolio)
  tutorials/
    01-first-llm-app/
      notes.md  code/  script.md  shorts.md  linkedin.md
```
