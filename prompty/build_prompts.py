"""Buduje prompty do stron 9-30 i okładki. Wynik: prompty.json."""
import json
from pathlib import Path

RAW = "https://raw.githubusercontent.com/chaperkooo/amelia-lumi-wzory/main/"
REF = {
    "A": RAW + "amelia/amelia_01_radosna_WZOR.png",
    "A_ZLOSC": RAW + "amelia/amelia_02_zlosc.png",
    "A_ZAGUBIONA": RAW + "amelia/amelia_03_zagubiona_a.png",
    "A_HALAS": RAW + "amelia/amelia_04_halas_b.png",
    "A_SMUTEK": RAW + "amelia/amelia_05_smutek_b.png",
    "A_PLACZ": RAW + "amelia/amelia_06_placz_stojac.png",
    "A_SKULONA": RAW + "amelia/amelia_07_placz_skulona_b.png",
    "A_SPOKOJ": RAW + "amelia/amelia_08_spokoj.png",
    "L": RAW + "lumi/lumi_01_spokojny_WZOR.png",
    "LK": RAW + "lumi/lumi_03_kolczasty.png",
    "LEO": RAW + "leo/leo_01_spokojny_WZOR.png",
}

GIRL = ("a 6-year-old girl, light golden blonde shoulder-length hair with gentle loose curls "
        "lying close to her head, a few light freckles on her cheeks and nose, small green eyes, "
        "white T-shirt with a small yellow star print, blue dungarees with straps and bib pocket, "
        "dark brown shoes")
GIRL_PJ = ("a 6-year-old girl, light golden blonde shoulder-length hair with gentle loose curls "
           "lying close to her head, a few light freckles on her cheeks and nose, small green eyes, "
           "soft pink pajamas with long sleeves and a small yellow star print on the chest")
LUMI = ("a small round fluffy squirrel-brown ball creature, big dark oval eyes, tiny smile, "
        "a small glowing white five-pointed star on its forehead, no tail, no ears, "
        "smaller than the girl's head")
LUMI_SPIKY = ("a small round squirrel-brown ball creature covered in rounded triangular spikes, "
              "eyes squeezed shut, the small five-pointed star on its forehead dim and cream-grey, "
              "no tail, no ears, smaller than the girl's head")
LEO = ("a 6-year-old boy, fluffy dark brown curly hair, warm brown skin, big dark brown eyes, "
       "calm gentle half-smile, green T-shirt with a small white rocket print, grey jogger "
       "trousers with cuffs, white sneakers, small round orange headphones resting around his neck")
TINY = "the creature is tiny, about the size of an apple, half the size of the girl's head"
STYLE = ("classic hand-drawn 2D animation style, bold dark outlines, simple flat colors, "
         "old-fashioned cartoon charm, children's picture book illustration")
SREF_DAY = ["strony/podglad/strona_04_podglad.png", "strony/podglad/strona_06_podglad.png", "strony/podglad/strona_07_podglad.png"]
SREF_NIGHT = ["strony/podglad/strona_08_podglad.png", "strony/podglad/strona_07_podglad.png", "strony/podglad/strona_04_podglad.png"]
NO = "--no photorealistic, 3d, text, letters, words, orange hair, giant creature, white background, white border, sticker, frame"
SPACE = "wide view, {top} above them"
HAIR_WITH_LEO = "the girl's hair is neat and smooth, not fluffy, only the boy has fluffy hair"


def p(refs, scene, extra_no="", night=False):
    urls = " ".join(REF[r] for r in refs)
    sref = " ".join(RAW + x for x in (SREF_NIGHT if night else SREF_DAY))
    no = NO + (", " + extra_no if extra_no else "")
    return (f"{urls} full-bleed scene illustration, the background fills the whole frame edge to edge, "
            f"{scene}, {STYLE} --ar 1:1 --iw 0.25 --sw 300 --sref {sref} {no}")


PAGES = {
    "09": p(["A", "LK"],
        "the girl from the first image standing in a noisy living room at a children's birthday party, "
        "covering her ears with both hands, eyes squeezed shut, upset overwhelmed face, "
        f"the creature from the second image floating in the air next to her shoulder, {TINY}, "
        "colorful balloons, one balloon popping with a small burst, confetti flying in the air, "
        "other happy children playing and dancing in the background, a boy with a paper party hat, "
        f"the girl: {GIRL}, the creature: {LUMI_SPIKY}, "
        + SPACE.format(top="plain pale wall"), "banner"),
    "10": p(["A_HALAS", "LK"],
        "close view, the girl from the first image covering her ears with both hands, eyes squeezed shut, "
        "gritted teeth, three happy children in paper party hats reaching out their hands and pulling her "
        "towards the party, a smiling mother bending down behind her, "
        f"the creature from the second image floating next to her head tangled in a prickly knot of its own spikes, {TINY}, "
        f"the girl: {GIRL}, the creature: {LUMI_SPIKY}, balloons and confetti, "
        + SPACE.format(top="plain pale wall"), "banner"),
    "11": p(["A_ZLOSC", "LK"],
        "the girl from the first image in a cozy kitchen stomping her foot angrily, a striped knitted sweater "
        "lying on the floor next to her, crayons jumping on the wooden table from the stomp, "
        "a kind grandmother with a grey hair bun, round glasses and a beige cardigan frowning and holding out her hands, "
        f"the creature from the second image floating next to the girl, {TINY}, "
        f"the girl: {GIRL}, the creature: {LUMI_SPIKY}, "
        + SPACE.format(top="plain cream kitchen wall")),
    "12": p(["A_PLACZ", "L"],
        "the girl from the first image standing by a big window crying, tears rolling down her cheeks, "
        "heavy rain on the window glass, grey rainy sky outside, a father in a sweater kneeling next to her, "
        "a child's crayon drawing of a giraffe and a penguin taped to the wall, "
        f"the creature from the second image floating next to her shoulder looking sad, its star dim, {TINY}, "
        f"the girl: {GIRL}, the creature: {LUMI}, sad droopy eyes, "
        + SPACE.format(top="plain grey rainy sky in the window")),
    "13": p(["A", "L"],
        "the girl from the first image hiding under a soft light blue blanket on a sofa, the blanket over her head "
        "like a little tent, only her face peeking out, calm relieved face, dim cozy room, "
        f"the creature from the second image snuggled next to her face under the blanket, {TINY}, "
        "its fur half fluffy and half with a few soft spikes, its white star glowing softly, "
        f"the girl: {GIRL}, the creature: {LUMI}, "
        + SPACE.format(top="plain dim wall"), "green blanket"),
    "14": p(["A_ZAGUBIONA", "L"],
        "the girl from the first image standing in front of the big doors of a large brick primary school, "
        "wearing a small backpack with yellow stars, looking up at the huge building, unsure worried face, "
        "many children going inside, "
        "the creature from the second image floating next to her very very small, the size of a walnut, "
        "hiding behind her shoulder, "
        f"the girl: {GIRL}, the creature: {LUMI}, worried eyes, "
        + SPACE.format(top="plain pale sky"), "sign, school name"),
    "15": p(["A_HALAS", "LK"],
        "the girl from the first image in the middle of a busy school hallway, covering her ears, eyes squeezed shut, "
        "children running and shouting around her, a school bell ringing on the wall with small sound lines, "
        "squeaky shoe marks on the shiny floor, buzzing ceiling lights with small zigzag lines, "
        f"the creature from the second image floating next to her with spikes sticking out in every direction, {TINY}, "
        f"the girl: {GIRL}, the creature: {LUMI_SPIKY}, "
        + SPACE.format(top="plain pale hallway wall"), "sign, posters with writing"),
    "16": p(["A_SMUTEK", "L"],
        "the girl from the first image sitting very straight at a school desk in a classroom, hands folded, "
        "trying hard, tired sad eyes, a teacher at the front pointing at her, other children at their desks, "
        f"the creature from the second image lying flat and tired on the desk next to her hands, {TINY}, "
        f"the girl: {GIRL}, the creature: {LUMI}, tired droopy half-closed eyes, its star dim, "
        + SPACE.format(top="plain classroom wall"), "blackboard writing, posters with writing"),
    "17": p(["A_SMUTEK", "L"],
        "the girl from the first image standing alone on a school playground holding a piece of chalk, "
        "simple chalk stars drawn on the ground around her feet, other children running away in the background "
        "playing tag, sad lonely face, "
        f"the creature from the second image floating next to her shoulder looking sad, its star dim, {TINY}, "
        f"the girl: {GIRL}, the creature: {LUMI}, sad eyes, "
        + SPACE.format(top="plain pale blue sky")),
    "18": p(["A_SMUTEK", "L"],
        "the girl from the first image walking slowly along a school corridor with her head down, "
        "a small quiet sad face with no smile, grey dull colors around her, "
        f"the creature from the second image floating behind her, its white star very dim and faded, {TINY}, "
        f"the girl: {GIRL}, the creature: {LUMI}, sad droopy eyes, "
        + SPACE.format(top="plain grey corridor wall"), "sign, posters with writing"),
    "19": p(["A_SKULONA", "L"],
        "the girl from the first image sitting in a dusty quiet corner under a wooden school staircase, "
        "hugging her knees tightly, tears on her cheeks, soft shadows, "
        "the creature from the second image curled up next to her into a small tight ball, its star dim, "
        "the size of an apple, "
        f"the girl: {GIRL}, the creature: {LUMI}, eyes closed, "
        + SPACE.format(top="the dark underside of the wooden stairs"), "locker"),
    "20": p(["A_SKULONA", "L"],
        "the girl from the first image sitting under a wooden school staircase hugging her knees, "
        "looking away from the creature with a sad thoughtful face, very dim blue shadows, "
        "the creature from the second image curled up a little away from her, "
        "its white star almost completely gone out, only a faint tiny glow, the size of an apple, "
        f"the girl: {GIRL}, the creature: {LUMI}, eyes closed, "
        + SPACE.format(top="the dark underside of the wooden stairs"), "locker"),
    "21": p(["A_SKULONA", "L"],
        "a quiet empty school hallway on a rainy day, a big window with heavy rain running down the glass, "
        "grey light, very small in the corner under the wooden staircase the girl from the first image "
        "hugging her knees and the creature from the second image curled up next to her, "
        f"the girl: {GIRL}, the creature: {LUMI}, calm sad lonely mood, lots of empty space, "
        "the window and the rain in the upper half of the picture", "locker"),
    "22": p(["A_SKULONA", "LEO", "L"],
        "under a wooden school staircase, the girl from the first image sitting hugging her knees, "
        "the boy from the second image quietly sitting down on the lowest step a little away from her, "
        "holding a notebook with a rocket drawing, calm kind face, not looking at her, "
        "the creature from the third image curled up next to the girl, its star dim, the size of an apple, "
        f"the girl: {GIRL}, the boy: {LEO}, the creature: {LUMI}, {HAIR_WITH_LEO}, "
        + SPACE.format(top="the dark underside of the wooden stairs"), "locker"),
    "23": p(["A_SKULONA", "LEO", "L"],
        "under a wooden school staircase, the boy from the second image sitting on the lowest step turned "
        "gently towards the girl from the first image and asking her a question, kind patient face, "
        "the girl sitting hugging her knees looking up at him surprised, rain on a window behind them, "
        "the creature from the third image curled up next to the girl with one eye open, the size of an apple, "
        f"the girl: {GIRL}, the boy: {LEO}, the creature: {LUMI}, {HAIR_WITH_LEO}, "
        + SPACE.format(top="plain dim wall"), "locker"),
    "24": p(["A", "LEO", "L"],
        "under a wooden school staircase, the boy from the second image smiling and pointing at the yellow star "
        "on the girl's T-shirt, the girl from the first image sitting on the floor with a small shy hopeful smile, "
        "the creature from the third image next to her slowly opening its eyes, its white star starting to glow again, "
        "the size of an apple, warm soft light, "
        f"the girl: {GIRL}, the boy: {LEO}, the creature: {LUMI}, {HAIR_WITH_LEO}, "
        + SPACE.format(top="plain warm wall"), "locker"),
    "25": p(["A_SPOKOJ", "LEO", "L"],
        "a bright friendly classroom, a cozy quiet corner with a big soft cushion and a small rug, the girl from the "
        "first image sitting calmly on the cushion, a picture plan of the day on the wall made only of simple "
        "pictures of a sun, a book, a plate and a ball, the boy from the second image smiling nearby, "
        "a kind young female teacher kneeling and listening, "
        "the creature from the third image floating next to the girl with a few spikes falling off its fur, "
        "the size of an apple, its white star glowing, "
        f"the girl: {GIRL}, the boy: {LEO}, the creature: {LUMI}, {HAIR_WITH_LEO}, "
        + SPACE.format(top="plain pale classroom wall"), "blackboard writing, words on the picture plan"),
    "26": p(["A_SPOKOJ", "L"],
        "evening in a cozy small bedroom, side view, the girl from the first image lying in a wooden bed under a soft "
        "light blue blanket, now wearing pink pajamas instead of dungarees, a gentle apologetic smile, "
        "the creature from the second image cuddled up against her cheek on the pillow, its white star glowing "
        "again, the size of an apple, a round window with a dark night sky and tiny stars, "
        f"the girl: {GIRL_PJ}, the creature: {LUMI}, deep navy blue night colors, "
        + SPACE.format(top="plain dark night wall"), "green blanket, white blanket, dungarees, overalls", night=True),
    "27": p(["A_SPOKOJ", "L"],
        "night, the girl from the first image sitting up in a wooden bed under a soft light blue blanket, "
        "now wearing pink pajamas instead of dungarees, one hand on her heart, eyes closed, a peaceful happy smile, "
        "the yellow star on her pajama top glowing brightly, the creature from the second image floating in front "
        "of her chest, its white star glowing with exactly the same light, a soft beam of golden light joining "
        "the two stars, the size of an apple, magical warm glow in a dark navy bedroom, "
        f"the girl: {GIRL_PJ}, the creature: {LUMI}, "
        + SPACE.format(top="plain dark night wall"), "green blanket, dungarees, overalls", night=True),
    "28": p(["A", "LEO", "L"],
        "a sunny school playground, the girl from the first image and the boy from the second image kneeling "
        "side by side drawing simple chalk stars and a star constellation on the ground, both smiling, "
        "the girl pointing up, a black bird singing on a low branch, a red ladybug with exactly four black spots "
        "on a leaf near the girl's hand, the creature from the third image bouncing happily above them, "
        "the size of an apple, its white star shining brightly, "
        f"the girl: {GIRL}, the boy: {LEO}, the creature: {LUMI}, {HAIR_WITH_LEO}, "
        + SPACE.format(top="open clear blue sky")),
    "29": p(["A_SPOKOJ", "L"],
        "the girl from the first image standing in a small sunny back garden with a calm gentle real smile, "
        "eyes open, a soft peaceful face, the creature from the second image floating next to her shoulder, "
        "its white star shining brighter than ever, the size of an apple, "
        f"the girl: {GIRL}, the creature: {LUMI}, "
        "a small sunny back garden with green grass, a rose bush with pink roses, a low light beige wooden fence, "
        "a few colorful flowers, " + SPACE.format(top="open clear blue sky")),
    "30": p(["A", "LEO", "L"],
        "early evening in a small back garden, the girl from the first image and the boy from the second image "
        "sitting on the grass side by side looking up at the first stars in a soft purple and blue sky, "
        "happy calm faces, the creature from the third image floating between them, its white star glowing like "
        "the stars in the sky, the size of an apple, a rose bush with pink roses, a low light beige wooden fence, "
        f"the girl: {GIRL}, the boy: {LEO}, the creature: {LUMI}, {HAIR_WITH_LEO}, "
        "view from behind and slightly to the side, the evening sky with first stars filling the upper half"),
    "okladka": p(["A", "L"],
        "book cover illustration, the girl from the first image standing in a small sunny back garden full of "
        "colorful flowers, big happy smile, eyes open, holding out her hand, the creature from the second image "
        "floating above her hand, the size of an apple, its white star glowing brightly, tiny sparkles around it, "
        f"the girl: {GIRL}, the creature: {LUMI}, "
        "a soft blue sky with a few small stars and gentle clouds, " + SPACE.format(top="open clear sky")),
}

SAD = ["12", "16", "17", "18", "19", "20", "21"]
for k in SAD:
    PAGES[k] = PAGES[k].replace("tiny smile, a small glowing white five-pointed star",
                                "a small sad frown, a small dim white five-pointed star")
PAGES["14"] = PAGES["14"].replace("tiny smile, a small glowing", "a small worried mouth, a small glowing")

out = Path(__file__).with_name("prompty.json")
out.write_text(json.dumps(PAGES, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"{len(PAGES)} prompts -> {out}")
