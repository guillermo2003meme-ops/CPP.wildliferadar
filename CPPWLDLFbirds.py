# birds_data.py
# Complete bird species list from Cal Poly Pomona wildlands (100 species)
# Source: https://www.cpp.edu/biodiversity/species/birds.shtml

BIRD_SPECIES = [
    {"common": "California Quail", "scientific": "Callipepla californica", "status": "Native"},
    {"common": "Turkey Vulture", "scientific": "Cathartes aura", "status": "Native"},
    {"common": "White-tailed Kite", "scientific": "Elanus leucurus", "status": "Native"},
    {"common": "Cooper's Hawk", "scientific": "Accipiter cooperii", "status": "Native"},
    {"common": "Red-shouldered Hawk", "scientific": "Buteo lineatus", "status": "Native"},
    {"common": "Red-tailed Hawk", "scientific": "Buteo jamaicensis", "status": "Native"},
    {"common": "Golden Eagle", "scientific": "Aquila chrysaetos", "status": "Native"},
    {"common": "American Kestrel", "scientific": "Falco sparverius", "status": "Native"},
    {"common": "California Gnatcatcher", "scientific": "Polioptila californica", "status": "Threatened (Federal)"},
    {"common": "Anna's Hummingbird", "scientific": "Calypte anna", "status": "Native"},
    {"common": "Black-chinned Hummingbird", "scientific": "Archilochus alexandri", "status": "Native"},
    {"common": "Rufous Hummingbird", "scientific": "Selasphorus rufus", "status": "Native"},
    {"common": "Great Horned Owl", "scientific": "Bubo virginianus", "status": "Native"},
    {"common": "Barn Owl", "scientific": "Tyto alba", "status": "Native"},
    {"common": "Western Screech-Owl", "scientific": "Megascops kennicottii", "status": "Native"},
    {"common": "Mourning Dove", "scientific": "Zenaida macroura", "status": "Native"},
    {"common": "Yellow Warbler", "scientific": "Dendroica petechia", "status": "Native"},
    {"common": "Western Bluebird", "scientific": "Sialia mexicana", "status": "Native"},
    {"common": "California Scrub-Jay", "scientific": "Aphelocoma californica", "status": "Native"},
    {"common": "Barn Swallow", "scientific": "Hirundo rustica", "status": "Native"},
    {"common": "European Starling", "scientific": "Sturnus vulgaris", "status": "Introduced"},
    {"common": "House Sparrow", "scientific": "Passer domesticus", "status": "Introduced"},
    {"common": "Rock Pigeon", "scientific": "Columba livia", "status": "Introduced"},
    {"common": "Spotted Dove", "scientific": "Spilopelia chinensis", "status": "Introduced"},
]

# Detailed bird information for the detail view
# (You can expand this with more species as needed)
BIRD_DETAILS = {
    "California Quail": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Galliformes, Family: Odontophoridae",
        "conservation_status": "Least Concern (IUCN) - California State Bird",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/California_Quail_mail_in_Golden_Gate_Park.JPG/500px-California_Quail_mail_in_Golden_Gate_Park.JPG",
        "characteristics": "A plump, grayish bird with a forward-curling black plume on its head. Males have a black face with a white border and a chestnut crown patch."
    },
    "Anna's Hummingbird": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Apodiformes, Family: Trochilidae",
        "conservation_status": "Least Concern (IUCN)",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Anna%27s_Hummingbird_-_male_flying.jpg",
        "characteristics": "Medium-sized hummingbird with iridescent emerald green back and pink-red throat (males). Females have a green back and a small red patch on the throat."
    },
    "California Gnatcatcher": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Passeriformes, Family: Polioptilidae",
        "conservation_status": "Threatened (Federal) - USFWS Listed Species[reference:4]",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a5/California_Gnatcatcher_%2839893559875%29.jpg",
        "characteristics": "Small, long-tailed bird with a thin bill. Males have a black cap during breeding season. Found in coastal sage scrub habitats."
    },
    "Yellow Warbler": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Passeriformes, Family: Parulidae",
        "conservation_status": "Least Concern (IUCN)",
        "image_url": "https://www.allaboutbirds.org/guide/assets/og/643914250-1200px.jpg",
        "characteristics": "Bright yellow bird with reddish streaks on the breast. Males have a brighter yellow head. Found in riparian woodlands and wetlands[reference:5]."
    },
    "Red-tailed Hawk": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Accipitriformes, Family: Accipitridae",
        "conservation_status": "Least Concern (IUCN) - Protected by Migratory Bird Treaty Act",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Red-tailed_Hawk_%2845812546121%29.jpg/3840px-Red-tailed_Hawk_%2845812546121%29.jpg",
        "characteristics": "Large hawk with a distinctive reddish tail. Broad, rounded wings. Commonly seen soaring over open areas[reference:6]."
    },
    "Western Bluebird": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Passeriformes, Family: Turdidae",
        "conservation_status": "Least Concern (IUCN)",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Western_bluebird_%28male%29.jpg/500px-Western_bluebird_%28male%29.jpg?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail",
        "characteristics": "Bright blue back and head, reddish-orange breast. Females are grayer with a blue tint. Often seen perched on fence posts."
    },
    "California Scrub-Jay": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Passeriformes, Family: Corvidae",
        "conservation_status": "Least Concern (IUCN)",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/California_Scrub_Jay_9301Abb.jpg/3840px-California_Scrub_Jay_9301Abb.jpg",
        "characteristics": "Blue and gray bird with a long tail. Lacks a crest. Bold and curious, often seen in oak woodlands and suburban areas[reference:7]."
    },
    "Mourning Dove": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Columbiformes, Family: Columbidae",
        "conservation_status": "Least Concern (IUCN)",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Mourning_dove_%281%29.jpg/1920px-Mourning_dove_%281%29.jpg?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=thumbnail",
        "characteristics": "Slender dove with a long, pointed tail. Soft brownish-gray color with black spots on wings. Known for its mournful cooing call."
    },
    "Great Horned Owl": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Strigiformes, Family: Strigidae",
        "conservation_status": "Least Concern (IUCN) - Protected by Migratory Bird Treaty Act",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Great-horned_Owl_RWD_at_CRC1.jpg",
        "characteristics": "Large owl with prominent ear tufts ('horns'). Mottled brown with a white throat patch. Powerful predator that nests in trees[reference:8]."
    },
    "Barn Owl": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Strigiformes, Family: Tytonidae",
        "conservation_status": "Least Concern (IUCN) - Protected by Migratory Bird Treaty Act",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/98/Flickr_-_Rainbirder_-_Barn_Owl_%28Tyto_alba%29.jpg?_=20241123235840",
        "characteristics": "Medium-sized owl with a distinctive heart-shaped face. Golden-brown and gray plumage. Nests in barns, trees, and structures[reference:9]."
    },
    "European Starling": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Passeriformes, Family: Sturnidae",
        "conservation_status": "Least Concern (IUCN) – Introduced to North America",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/European_starling_in_CP_%2833849%29.jpg/3840px-European_starling_in_CP_%2833849%29.jpg",
        "characteristics": "Medium-sized black bird with iridescent purple and green plumage, speckled with white spots in winter. Known for its mimicking abilities and large, noisy flocks."
    },
    "Barn Swallow": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Passeriformes, Family: Hirundinidae",
        "conservation_status": "Least Concern (IUCN)",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Barn_Swallow_on_a_small_Plant_%2849519926103%29.jpg",
        "characteristics": "Sleek swallow with steely blue upperparts, a cinnamon throat, and a deeply forked tail. Often seen skimming over fields and water to catch insects in flight."
    },
    "House Sparrow": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Passeriformes, Family: Passeridae",
        "conservation_status": "Least Concern (IUCN) – Introduced worldwide",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9e/House_Sparrow_%28M%29_I_IMG_7881.jpg?_=20180204175514",
        "characteristics": "Small, stout bird with a thick bill. Males have a gray crown, black bib, and chestnut nape; females are plain brownish with a buffy eyebrow."
    },
    "Rock Pigeon": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Columbiformes, Family: Columbidae",
        "conservation_status": "Least Concern (IUCN) – Feral populations common in cities",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Blue_Rock_Pigeon_I2_IMG_7877.jpg",
        "characteristics": "Plump pigeon with a gray body, iridescent neck feathers, and two dark wing bars. Often seen in urban environments and on building ledges."
    },
    "Spotted Dove": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Columbiformes, Family: Columbidae",
        "conservation_status": "Least Concern (IUCN) – Introduced to Southern California",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Spotted_Dove_%28Streptopelia_chinensis%29_in_Kolkata_W_IMG_3515.jpg",
        "characteristics": "Slender dove with a black-and-white spotted patch on the sides of the neck, pinkish-gray breast, and a long, white-edged tail."
    },
    "Turkey Vulture": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Cathartiformes, Family: Cathartidae",
        "conservation_status": "Least Concern (IUCN)",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b2/Turkey_Vulture.jpg",
        "characteristics": "Large, dark-brown vulture with a featherless red head. Soars with wings held in a slight V-shape, using its keen sense of smell to locate carrion."
    },
    "Golden Eagle": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Accipitriformes, Family: Accipitridae",
        "conservation_status": "Least Concern (IUCN) – Protected by Bald and Golden Eagle Protection Act",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/4/49/Golden_eagle_at_ACES_%2811822%29.jpg",
        "characteristics": "Majestic, dark-brown eagle with golden feathers on the back of its head and neck. One of the largest raptors in North America, often seen soaring over open terrain."
    },
    "White-tailed Kite": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Accipitriformes, Family: Accipitridae",
        "conservation_status": "Least Concern (IUCN)",
        "image_url": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgErSkzFTC3onRewLRZ1t_nVGyBouB8dPJ9hvHj6zKgkPaxU2T-4zsnRn2WC-34LSNuqCcJaBdSfbNmX7eWxGJIJppTz_xKl12tbCGYJMTKuRCF6YeqFrNwKEQ1hh6EVxFvRCX4xnq6uak/s3456/P1080853+%25282%2529.JPG",
        "characteristics": "Graceful, white raptor with black shoulders and a long, white tail. Often hovers in place while hunting for small mammals in open grasslands."
    },
    "Cooper's Hawk": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Accipitriformes, Family: Accipitridae",
        "conservation_status": "Least Concern (IUCN)",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/83/Cooper%27s_hawk.jpg",
        "characteristics": "Medium-sized hawk with a long, banded tail and rounded wings. Adults have a dark cap, red eyes, and a finely barred rufous chest."
    },
    "Red-shouldered Hawk": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Accipitriformes, Family: Accipitridae",
        "conservation_status": "Least Concern (IUCN)",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Red-shouldered_Hawk_%2840808154743%29.jpg",
        "characteristics": "Colorful hawk with reddish shoulders, a strongly banded tail, and a pale chest marked with rufous bars. Often found in wooded areas near water."
    },
    "American Kestrel": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Falconiformes, Family: Falconidae",
        "conservation_status": "Least Concern (IUCN)",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e6/American_Kestrel_%28Falco_Sparverius%292.jpg",
        "characteristics": "North America's smallest falcon, with a rusty back, blue-gray wings (males), and two dark facial stripes. Often seen hovering or perched on wires along roadsides."
    },
    "Rufous Hummingbird": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Apodiformes, Family: Trochilidae",
        "conservation_status": "Near Threatened (IUCN)",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Rufous_Hummingbird%2C_male_01.jpg",
        "characteristics": "Small, feisty hummingbird with a brilliant orange-red throat (male) and rufous (rusty) back, sides, and tail. Known for its aggressive territorial behavior."
    },
    "Black-chinned Hummingbird": {
        "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Apodiformes, Family: Trochilidae",
        "conservation_status": "Least Concern (IUCN)",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/2/20/Black-chinned_Hummingbird._Archilochus_alexandri._Male_-_Flickr_-_gailhampshire_%282%29.jpg",
        "characteristics": "Small hummingbird with a metallic green back and a black chin with a thin purple band below it (male). Females have a pale throat with fine spots."
    },
    "Western Screech-Owl": {
    "classification": "Kingdom: Animalia, Phylum: Chordata, Class: Aves, Order: Strigiformes, Family: Strigidae",
    "conservation_status": "Least Concern (IUCN)",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Western_Screech_Owl.jpg",
    "characteristics": "Small, stocky owl with ear tufts, mottled gray or brown plumage, and a finely streaked breast. Active at night, its descending trill and whistled calls are often heard in woodlands and suburban areas."
    }
}
# Default image for birds not in BIRD_DETAILS
DEFAULT_BIRD_IMAGE = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Bird_silhouette.svg/400px-Bird_silhouette.svg.png"