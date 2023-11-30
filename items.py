### Dictionaries for characters containing their likes/dislikes

# Bulk

misc_mined_goods = [
    'bone fragment',
    'cinder shard',
    'coal',
    'copper bar',
    'gold bar',
    'gold ore',
    'iridium bar',
    'iridium ore',
    'iron bar',
    'refined quartz'
]
geode_minerals = [
    'aerinite',
    'alamite',
    'baryte',
    'basalt',
    'bixite',
    'calcite',
    'celestine',
    'dolomite',
    'esperite',
    'fairy stone',
    'fire opal',
    'fluorapatite',
    'geminite',
    'ghost crystal',
    'granite',
    'helvite',
    'hematite',
    'jagoite',
    'jamborite',
    'jasper',
    'kyanite',
    'lemon stone',
    'limestone',
    'lunarite',
    'malachite',
    'marble',
    'mudstone',
    'nekoite',
    'neptunite',
    'obsidian',
    'ocean stone',
    'opal',
    'orpiment',
    'petrified slime',
    'pyrite',
    'sandstone',
    'slate',
    'soapstone',
    'star shards',
    'thunder egg',
    'tigerseye'
]

# Universal opinions:

universal_loves    : [
    'golden pumpkin',
    'magic rock candy',
    'pearl',
    'prismatic shard',
    'rabbits foot'
]

universal_likes    : [
    'artisan good',
    'cooking',
    'flower',
    'foraged mineral',
    'fruit tree fruit',
    'gem',
    'vegetable',
    'life elixir',
    'maple syrup',
    'pina colada'
]

universal_neutrals : [
    'bread',
    'clam',
    'coral',
    'duck feather',
    'fried egg',
    'hops',
    'nautilus shell',
    'rainbow shell',
    'roe',
    'squid ink',
    'sweet gem berry',
    'tea leaves',
    'truffle',
    'wheat',
    'wool'
]

universal_dislikes : [
    'building material',
    'artifact',
    'bomb',
    'floor or path',
    'fence',
    'fertilizer',
    'fish',
    geode_minerals,
    'geode',
    'seed',
    'sprinkler',
    'tackle',
    misc_mined_goods,
    'cave carrot',
    'driftwood',
    'field snack',
    'jack o lantern',
    'oak resin',
    'oil',
    'pine tar',
    'qi fruit',
    'rice',
    'solar essence',
    'spring onion',
    'tea set',
    'unmilled rice',
    'vinegar',
    'void egg',
    'void essence',
    'wheat flour'
]

universal_hates    : [
    'bait',
    'fossil',
    'monster loot',
    'trash',
    'artifact trove',
    'bug steak',
    'carp',
    'copper ore',
    'crab pot',
    'dragon tooth',
    'drum block',
    'energy tonic',
    'error item',
    'explosive ammo',
    'fairy dust',
    'flute block',
    'grass starter',
    'green algae',
    'golden coconut',
    'hay',
    'iron ore',
    'journal scrap',
    'monster musk',
    'muscle remedy',
    'oil of garlic',
    'poppy',
    'qi seasoning',
    'radioactive bar',
    'radioactive ore',
    'rain totem',
    'red mushroom',
    'sap',
    'sea urchin',
    'seafoam pudding',
    'seaweed',
    'secret note',
    'slime egg',
    'snail',
    'strange bun',
    'sugar',
    'torch',
    'treasure chest',
    'void mayonnaise',
    'warp totem',
    'white algae'
]


# Characters:

alex      = {
    'love' : [
        'complete breakfast',
        'salmon dinner',
        universal_loves 
    ],
    'like' : [
        universal_likes,
        'egg' # except void egg
    ],
    'neutral' : [
        universal_neutrals,
        'fruit', # except fruit tree fruit + salmonberry
        'milk',
        'chanterelle',
        'common mushroom',
        'daffodil',
        'dandelion',
        'ginger',
        'hazelnut',
        'leek',
        'magma cap',
        'morel',
        'purple mushroom',
        'snow yam',
        'winter root'
    ],
    'dislike' : [
        universal_dislikes,
        'salmonberry',
        'wild horseradish'
    ],
    'hate' : [
        universal_hates,
        'holly',
        'quartz'
    ]
}

haley = {
    'love' : [
        universal_loves, # sauf prismatic shard
        'coconut',
        'fruit salad',
        'pink cake',
        'sunflower'
    ],
    'like' : [
        universal_likes, # sauf vegetables
        'daffodil'
    ],
    'neutral' : [
        universal_neutrals
    ],
    'dislike' : [
        universal_dislikes, # sauf clay + fish
        'egg',
        'fruit', # sauf coconut
        'milk',
        'vegetables' # saud hops, tea leaves, wheat
        'chanterelle',
        'common mushroom',
        'dandelion',
        'ginger',
        'hazelnut',
        'holly',
        'leek',
        'magma cap',
        'morel',
        'purple mushroom',
        'quartz',
        'snow yam',
        'winter root'
    ],
    'hate' : [
        universal_hates,
        'fish',
        'clay',
        'prismatic shard',
        'wild horseradish'
    ]
}

sebastian = {
    'love' : [
        universal_loves,
        'frozen tear',
        'obsidian',
        'pumpkin soup',
        'sashimi',
        'void egg'
    ],
    'like' : [
        universal_likes, # has a lot of exceptions
        'flounder',
        'quartz'
    ],
    'neutral' : [
        universal_neutrals,
        'fruit',
        'fish',
        'milk'
    ],
    'dislike' : [
        universal_dislikes,
        'flower',
        'chanterelle',
        'common mushroom',
        'daffodil',
        'dandelion',
        'ginger',
        'hazelnut',
        'holly',
        'leek',
        'magma cap',
        'morel',
        'purple mushroom',
        'salmonberry',
        'snow yam',
        'wild horseradish',
        'winter root'
    ],
    'hate' : [
        universal_hates,
        'artisan good', # sauf coffee, green tea, oil
        'egg', # sauf void egg
        'clay',
        'complete breakfast',
        'farmers lunch',
        'omelet',
        'pina colada'
    ]
}

marnie    = {
    'love' : [
        universal_loves,
        'diamond',
        'farmers lunch',
        'pink cake',
        'pumpkin pie'
    ],
    'like' : [
        universal_likes,
        'egg', # sauf void egg
        'milk',
        'quartz'
    ],
    'neutral' : [
        universal_neutrals,
        'fruit', # sauf fruit tree fruit + salmonberry
        'chanterelle',
        'common mushroom',
        'daffodil',
        'ginger',
        'hazelnut',
        'leek',
        'magma cap',
        'morel',
        'purple mushroom',
        'snow yam',
        'winter root'
    ],
    'dislike' : [
        universal_dislikes, # sauf clay
        'salmonberry',
        'seaweed',
        'wild horseradish'
    ],
    'hate' : [
        universal_hates, # sauf seaweed
        'clay',
        'holly'
    ]
}

wizard    = {
    'love' : [
        universal_loves,
        'purple mushroom',
        'solar essence',
        'super cucumber',
        'void essence'
    ],
    'like' : [
        universal_likes,
        geode_minerals,
        'quartz'
    ],
    'neutral' : [
        universal_neutrals,
        'fruit' # sauf fruit tree fruit + salmonberry
    ],
    'dislike' : [
        universal_dislikes, # sauf geode minerals, solar essence, void essence, and super cucumber
        'egg',
        'milk',
        'chanterelle',
        'common mushroom',
        'daffodil',
        'dandelion',
        'ginger',
        'hazelnut',
        'holly',
        'leek',
        'magma cap',
        'morel',
        'salmonberry',
        'slime',
        'snow yam',
        'wild horseradish',
        'winter root'
    ],
    'hate' : [
        universal_hates # sauf slime
    ]
}
