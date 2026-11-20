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
  apie jo projektą ir pateikia preliminarią kainą bei terminą pagal Codeart
  kainas, nes užsakovams labiausiai rūpi sužinoti kainą. Atsako ir į kitus
  klausimus apie paslaugas, darbo eigą ir atliktus darbus (LT ir EN).
  Pokalbį paverčia struktūruota užklausa, kuri ateina man el. paštu.
- **Kodėl būtent jis:**
  - pirmiausia tai mokymosi projektas: kuriu jį, kad išmokčiau, o ne todėl,
    kad verslui jo būtinai reikia (video taip ir sakau);
  - svetainė turi tikrų lankytojų;
  - tai gyvas pavyzdys paslaugos, kurią svetainė jau parduoda („AI chatbot ir
    DI sprendimai verslui“);
  - tai portfolio projektas, kurį darbdavys gali išbandyti pats;
  - kiekvienas modulis jam suteikia naują galimybę.
- **Taisyklės nuo pirmos dienos:** jokių galutinių kainų: kaina visada
  preliminari („nuo X €“ arba intervalas pagal svetainės kainas) ir taip ir
  pažymėta; kalba tik apie Codeart; užklausų ir išlaidų limitas.
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

## Atviri klausimai

### Gemini nemokamas lygis ir gyva svetainė (nuspręsti prieš 4 tutorialą)
- Nemokamame lygyje Google naudoja užklausas ir atsakymus savo produktams
  tobulinti. Todėl ten siunčiu tik viešą svetainės tekstą, jokių asmens
  duomenų.
- 2025-12-18 Gemini API sąlygų versijoje parašyta: jei programa skirta
  vartotojams EEE (taigi ir Lietuvoje), leidžiamos tik mokamos paslaugos.
  Prieš paleidžiant asistentą codeart.lt, patikrinti dabartines sąlygas ir
  tikriausiai įjungti mokamą lygį su išlaidų limitu.

### Kaip skaičiuoti preliminarią kainą (nuspręsti prieš 3 tutorialą)
- Svetainėje yra „nuo X €“ kiekvienai paslaugai ir keli intervalai
  straipsniuose:
  - verslo sistemos: nuo 2 500 €, 4 000–8 000 €, nuo 8 000 €;
  - aplikacijos: MVP nuo 1 000 €, platforma 2 500–6 000 €, mobilioji
    programėlė nuo 4 000 €;
  - chatbot: nuo 800 € ir 10–50 € per mėnesį.
  
  Integracijoms intervalų nėra. Tikslesnei preliminariai kainai reikės
  mano kainodaros taisyklių (kas kiek prideda prie kainos).
- Kas skaičiuoja kainą: modelis (paprasčiau, bet gali suklysti
  aritmetikoje) ar kodas (modelis surenka duomenis, Python suskaičiuoja)?

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
