import random
from titlecase import titlecase


def necronPhrase():
    verbs = ['Beware', 'Fear', 'Dread', 'Worship', 'Praise', 'Honor', 'Cower Before', 'Offer Your Daughters To', 'Venerate', 'Adulate', 'Revere', 'Kiss', 'Smooch', 'Bow Before', 'Adore', 'Kiss the Grits of', 'Bestow Your Wealth Upon', 'Say Nice Things to', 'Forsake Your Deities for']

    adjectives = ['Fearsome', 'Unknowable', 'Enigmatic', 'Ancient', 'Beautiful', 'Superior', 'Invincible', 'Pretty', 'Undying', 'Masterful', 'Diabolical', 'Supreme', 'Fine-Legged', 'Bespoke', 'Boomer', 'Handsome', 'Puri-Puri']

    names = ['Sautekh', 'Maynarkh', 'Nihilakh', 'Mephrit', 'Thokt', 'Macron', 'Cronling']

    verbs2 = ['Disintigrate', 'Obliterate', 'Emasculate', 'Smooch', 'Enslave', 'Covet', 'Stare Unnervingly At', 'Liquify', 'Imprison', 'Defenestrate', 'Serenade', 'Uplift', 'Scatter', 'Mock', 'Point and Laugh at', 'Sleep Several Millenia to Avoid', '']

    nouns = ['Synapses', 'Women', 'Men', 'Planets', 'Souls', 'Gods', 'Genitals', 'Flesh-Bound Forms', 'Greatest Heroes', 'Mothers', 'Friends', 'Soft-Tissue', 'Thots', 'Hot Eldar Waifus', 'Sororitas', 'Grey Knights', 'Space Marines', 'Corpse-God']

    verb = random.choice(verbs)
    adjective = random.choice(adjectives)
    name = random.choice(names)
    verb2 = random.choice(verbs2)
    noun = random.choice(nouns)


    thePhrase = f'{verb} the {adjective} {name} Dynasty! We will {verb2} your {noun}!'

    return thePhrase

def nurglePhrase():
    percent = random.randrange(1, 100)
    days = random.randrange(1,90)
    planets = random.choice(['Sigma ', 'Beta ', 'Poo ', 'Alpha ', 'Primus ', 'Tertius ', 'Agriworld ', 'Sept World ', 'Temple Planet ', 'Hive Majorus ', 'Hive Minorus ', 'Theta '])
    numbers = random.randrange(1, 20)
    planet = planets + str(numbers)

    adjective1 = random.choice(['Shitty', 'Poo-Loving', 'Fierce', 'Worthy', 'Lazy', 'Fun-loving', 'Hateful', 'Disgusting', 'Pus-Covered', 'Leaking', 'Wailing', 'Loyal'])

    noun1 = random.choice(['Poo', 'Vomit', 'Nurgle', 'Motarion', 'Dirt', 'Pus', 'Phlegm', 'Boils', 'Bile', 'Ooze', 'Filthy Orifices', 'Butts', 'Eye-Sockets', 'Infected Holes', 'Gooey Orifices', 'Slimy Orifices'])

    adjective2 = random.choice(['Phlegmy', 'Snotty', 'Slimy', 'Stinking', 'Vomitous', 'Oozing', 'Pus-Spewing', 'Bile-Spewing', 'Poo-Ejecting', 'Rotting', 'Leperous', 'Itching', 'Wailing', 'Screaming', 'Weeping'])

    verb = random.choice(['Projectile Vomit', 'Spew', 'Vomit', 'Ooze', 'Bleed', 'Expel', 'Hurl', 'Regurgitate', 'Eject', 'Belch', 'Gush', 'Dispense', 'Release'])

    noun2 = random.choice(['Eye-Sockets', 'Mouths', 'Assholes', 'Pores', 'Nostrils', 'Orifices', 'Skin', 'Scabs', 'Wounds', 'Ears', 'Genitals', 'Fingernails', 'Joints', 'Throats', 'Scalps', 'Feet', 'Belly-Buttons', 'Boils'])

    noun3 = random.choice(['Nurglings', 'Poo', 'Scabs', 'Pus', 'Half-Chewed Food', 'Flies', 'Bile', 'Acid', 'Rotting Fingers', 'Hair', 'Snot', 'Boogers', 'Rust', 'Noxious Gas', 'Plague-Mites', 'Fingernails'])

    verb2 = random.choice(['Mindlessly Worship', 'Try to Eat', 'Ceaselessly Vomit', 'Build Shrines out of', 'Endlessly Praise', 'Force-Feed the Survivors', 'Desecrate', 'Mutate into'])



    walkers = f'{adjective1} Poxwalkers who {verb2} {noun2},'

    disease = f'infected with the {adjective2} {noun1} virus, with one of the symptoms causing them to {verb} {noun3} out of their {noun2}!'

    phrase1 = f'The Death Guard invaded the planet {planet}! They attacked with {walkers} killing {percent}% of the population over {days} days! The surivors were {disease}'

    return phrase1

def greyPhrase():
    enemies = ['Space Marines', 'Death Guard', 'Thousand Sons', 'Heretic Marines', 'Tyranids', 'Grey Knights', 'Daemons', 'Daemonettes', 'Civilians', 'Condemned Traitors', 'Rogue Psykers', 'Custodes', 'Daemon Primarchs', 'Mechanicus', 'Sororitas', 'Imperial Guardsmen', 'Entire Planets', 'Necrons', 'Grey Knights']

    results1 = ['Resounding', 'Mediocre', 'Massive', 'Pyrrhic', 'Legendary', 'Shocking', 'Pitiable', 'Shameful', 'Grand', 'Worthy', 'Peerless', 'Unmatched', 'Indefinable', 'Majestic', 'Timeless', 'Unforgettable', 'Gut-Wrenching', 'Fantastical', 'Grimdark', 'Noblebright', 'Costly', 'Meaningless', 'Fortuitous', 'Pitiful', 'Sensational', 'Unparalleled']
    results2 = ['Success', 'Victory', 'Failure', 'Slaughter', 'Upset', 'Event', 'Outing', 'Sacrifice', 'Achievement', 'Battle', 'Scouring', 'Tête-à-tête', 'Mashing', 'Accomplishment', 'Triumph', 'Killing', 'Win', 'Loss', 'Strike', 'Defeat', 'Failing', 'Abortion', 'Misadventure', 'Flop', 'Sensation', 'Performance', 'Act', 'Affair', 'Thing', 'Accident', 'Calamity', 'Marvel', 'Juncture', 'Miracle', 'Incident', 'Matter']
    nouns1 = ['Battle of', 'Slaughter of', 'Trashing of', 'Sacrifice of', 'Liberation of', 'Condemnation of', 'Spanking of', 'Purging of', 'Wasting of', 'Burnination of', 'Obliteration of', 'Mercy of', 'Hateful Slaying of', 'Beheading of', 'Comeuppance of', 'Rightful Fuckening of', 'Scouring of', 'Cleansing of', 'Ascension of', 'Ruination of', 'Fortune of', 'Pity of', 'Final Chapter of', 'Duplicitousness of', 'Deception of', 'Final Countdown of', 'Bastion of', 'Blasting of', 'Fuckening of', 'Killing of', 'Calamity of', 'Celebration of', 'Misfortune of', 'Coincidence of', 'Marvel of']
    nouns2 = ['Killington', 'Murderbonia', 'Pleasantville', 'Doom Hole', 'the Kindergardners', 'Daemons', 'Heretics', 'the Guilty', 'the Innocent', 'the Condemned', 'the Larrys', 'the Jerrys', 'the Mo\'s', 'the Macs', 'the Babies', 'Transexual Transylvania', 'Hell\'s Anus', 'the Wicked', 'the Damned', 'Traitors', 'Xenos', 'PoundTown', 'Innocence', 'Hatred', 'Anger', 'Limbs', 'Sensibilities', 'Wastrels', 'the Traitorous', 'the Sinful', 'the Immaterium', 'Khorne', 'Tzeentch', 'Slaanesh', 'Nurgle', 'Millenia', 'Beasts', 'the Galaxy', 'the Imperium', 'the Fragile', 'the Hateful', 'Friends', 'Foes', 'the Grey Knights']
    year = random.randrange(35000, 41000)
    number = random.randrange(1000)
    number2 = random.randrange(100000)
    losses = random.randrange(number)
    selfloss = random.randrange(losses)
    enemy = random.choice(enemies)
    result1 = random.choice(results1)
    result2 = random.choice(results2)
    noun1 = random.choice(nouns1)
    noun2 = random.choice(nouns2)

    thePhrase = f'In the year {year}, {number} Grey Knights fought and slew {number2} heretical {enemy}, at the cost of {losses} Grey Knights! ({selfloss} inflicted by friendly brains exploding) The mission was viewed as a {result1} {result2}, and was dubbed The {noun1} {noun2}.'

    return thePhrase

def jerryPhrase():

    team = random.choice(['Custodicks', 'Blood Jerrys', 'Aeldari', 'Drukhari', 'Heretic Astartes', 'Mechanicus', 'Imperial Guard'])

    thePhrase = f'Jerry should play {team}!'

    return thePhrase

def insult():
    words = ('''artless             base-court          apple-john
    bawdy               bat-fowling         baggage
    beslubbering        beef-witted         barnacle
    bootless            beetle-headed       bladder
    churlish            boil-brained        boar-pig
    cockered            clapper-clawed      bugbear
    clouted             clay-brained        bum-bailey
    craven              common-kissing      canker-blossom
    currish             crook-pated         clack-dish
    dankish             dismal-dreaming     clotpole
    dissembling         dizzy-eyed          coxcomb
    droning             doghearted          codpiece
    errant              dread-bolted        death-token
    fawning             earth-vexing        dewberry
    fobbing             elf-skinned         flap-dragon
    froward             fat-kidneyed        flax-wench
    frothy              fen-sucked          flirt-gill
    gleeking            flap-mouthed        foot-licker
    goatish             fly-bitten          fustilarian
    gorbellied          folly-fallen        giglet
    impertinent         fool-born           gudgeon
    infectious          full-gorged         haggard
    jarring             guts-griping        harpy
    loggerheaded        half-faced          hedge-pig
    lumpish             hasty-witted        horn-beast
    mammering           hedge-born          hugger-mugger
    mangled             hell-hated          joithead
    mewling             idle-headed         lewdster
    paunchy             ill-breeding        lout
    pribbling           ill-nurtured        maggot-pie
    puking              knotty-pated        malt-worm
    puny                milk-livered        mammet
    qualling            motley-minded       measle
    rank                onion-eyed          minnow
    reeky               plume-plucked       miscreant
    roguish             pottle-deep         moldwarp
    ruttish             pox-marked          mumble-news
    saucy               reeling-ripe        nut-hook
    spleeny             rough-hewn          pigeon-egg
    spongy              rude-growing        pignut
    surly               rump-fed            puttock
    tottering           shard-borne         pumpion
    unmuzzled           sheep-biting        ratsbane
    vain                spur-galled         scut
    venomed             swag-bellied        skainsmate
    villainous          tardy-gaited        strumpet
    warped              tickle-brained      varlot
    wayward             toad-spotted        vassal
    weedy               unchin-snouted      whey-face
    yeasty              weather-bitten      wagtail
    ''')

    splitList = words.split()
    columnOne = []
    columnTwo = []
    columnThree = []
    index = 0
    indexZero = 0
    indexOne = 1
    indexTwo = 2

    for word in splitList:
        if index == indexZero:
            columnOne.append(word)
            index = index + 1
            indexZero = indexZero + 3

        elif index == indexOne:
            columnTwo.append(word)
            index = index + 1
            indexOne = indexOne + 3

        elif index == indexTwo:
            columnThree.append(word)
            index = index + 1
            indexTwo = indexTwo + 3



    one = random.choice(columnOne)
    two = random.choice(columnTwo)
    three = random.choice(columnThree)
    first = titlecase(str(one))
    second = titlecase(str(two))
    third = titlecase(str(three))

    insult = f'Fook Off Ye {first} {second} {third}'

    return insult
