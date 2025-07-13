""" This program is a hard rule based choice to select traits of the organism you are creating. 
    Compares the choose traits with different traits of the existing organism. You can also 
    name the organsim and save its traits along with name on a text file"""


import tabulate

class TraitSelection:
    dictionary = {}
    def traitDetails(self):
        traitsDetail = [
        ["Autotrophic", "they produce their own food using sunlight or chemicals"],
        ["Heterotrophic", "they depend on other organisms for food"],
        ["Lithotrophic", "they derive energy from inorganic compounds"],
        ["Aquatic", "they live in water environments"],
        ["Terrestrial", "they live on land"],
        ["Aerial", "they live in the air or rely on flight"],
        ["Subterranean", "they live underground"],
        ["Asexual", "they reproduce without needing a mate"],
        ["Sexual", "they require a mate for reproduction"],
        ["Binary fission", "they split into two identical organisms"],
        ["Parthenogenesis", "they reproduce without fertilization"],
        ["Single-celled", "they consist of one microscopic cell"],
        ["Multicellular", "they have multiple cells forming tissues and organs"],
        ["Exoskeleton", "they have an external skeleton for protection"],
        ["Endoskeleton", "they have an internal skeleton"],
        ["Herbivorous", "they eat plants"],
        ["Carnivorous", "they eat animals"],
        ["Omnivorous", "they eat both plants and animals"],
        ["Detritivorous", "they feed on decomposing matter"],
        ["Parasites", "they live off a host organism"] 
        ]
        header = ["Traits", "Explaination"]
        print(tabulate.tabulate(traitsDetail, headers = header, tablefmt = "grid"))

    def traitNutrient(self):
        print("Mode of Nutrient:")
        print("a.Autotrophic (Self-feeding), b. Heterotrophic (dependent on other organisms), c. Lithotrophic")
        print("d. Skip")
        choice = input("Enter Your Choice: ")
        print()
        if (choice.lower() == 'a'):
            print("1. Photoautotropes, 2. Chemoautotrophs")
            choice = int(input("Enter Your Choice: "))
            print()
            if (choice == 1):
                self.dictionary["Mode of Nutrient"] = {"Autotrophic":"Photoautotropes"}
            
            elif (choice == 2):
                self.dictionary["Mode of Nutrient"] = {"Autotrophic":"Chemoautotrophs"}

            else:
                print("Enter Valid Choice!")
            
            print()
        
        elif (choice.lower() == 'b'):

            print("1. Herbivores, 2. Carnivores, 3. Omnivores, 4. Detritivores, 5. Parasites")
            choice = int(input("Enter Your Chocie: "))
            print()
            if (choice == 1):
                self.dictionary["Mode of Nutrient"] = {"Heterotrophic":"Herbivores"}
            
            elif (choice == 2):
                self.dictionary["Mode of Nutrient"] = {"Heterotrophic ":"Carnivores"}
            
            elif (choice == 3):
                self.dictionary["Mode of Nutrient"] = {"Heterotrophic ":"Omnivores"}

            elif (choice == 4):
                self.dictionary["Mode of Nutrient"] = {"Heterotrophic":"Detritivores"}

            elif (choice == 5):
                self.dictionary["Mode of Nutrient"] = {"Heterotrophic ":"Parasites"}

            else:
                print("Enter Valid Choice!")
            

        elif (choice.lower() == 'c'):
            self.dictionary["Mode of Nutrient"] = "Lithotrophic"
        
        elif (choice.lower() == 'd'):
            print("Skipped...")

        else:
            print("Enter Valid Choice!")
            self.traitNutrient()

    def traitAmmonia(self):
        print("Mode of Ammonia Excretion:")
        print("a. Ammonotelic, b. Ureotelic, c. Uricotelic")
        print("d. Skip")
        choice = input("Enter Your Choice: ")
        print()
        if (choice.lower() == 'a'):
            self.dictionary["Mode of Ammonia Excretion"] = "Ammonotelic"
        
        elif (choice.lower() == 'b'):
            self.dictionary["Mode of Ammonia Excretion"] = "Ureotelic"

        elif (choice.lower() == 'c'):
            self.dictionary["Mode of Ammonia Excretion"] = "Uricotelic"

        elif (choice.lower() == 'd'):
            print("Skipped...")

        else:
            print("Enter Valid Choice!")
            self.traitAmmonia()

    def traitHabitat(self):
        print("Based on the Habitat:")
        print("a. Terrestrial  , b. Aquatic , c. Aerial, d. Subterranean")
        print("e. Skip")
        choice = input("Enter Your Choice: ")
        print()
        if (choice.lower() == 'a'):
            self.dictionary["Habitat"] = "Terrestrial "
        
        elif (choice.lower() == 'b'):
            
            print("1. Marine  , 2. Freshwater ")
            choice = int(input("Enter Your Chocie: "))
            print()
            if (choice == 1):
                self.dictionary["Habitat"] = {"Aquatic": "Marine "}
            
            elif (choice == 2):
                self.dictionary["Habitat"] = {"Aquatic": "Freshwater "} 

            else:
                print("Enter Valid Choice!")

        elif (choice.lower() == 'c'):
            self.dictionary["Habitat"] = "Aerial"

        elif (choice.lower() == 'd'):
            self.dictionary["Habitat"] = "Subterranean"
        
        elif (choice.lower() == 'e'):
            print("Skipped...")
        
        else:
            print("Enter Valid Choice!")
            self.traitHabitat()

    def traitReproduction(self):
        print("Reproduction Type:")
        print("a. Asexual , b. Sexual, c. Binary fission, d. Parthenogenesis")
        print("e. Skip")
        choice = input("Enter Your Choice: ")
        print()
        if (choice.lower() == 'a'):
            self.dictionary["Reproduction"] = "Asexual"

        elif (choice.lower() == 'b'):
            self.dictionary["Reproduction"] = "Sexual"

        elif (choice.lower() == 'c'):
            self.dictionary["Reproduction"] = "Binary fission"

        elif (choice.lower() == 'd'):
            self.dictionary["Reproduction"] = "Parthenogenesis"
        
        elif (choice.lower() == 'e'):
            print("Skipped...")
        
        else:
            print("Enter Valid Choice!")
            self.traitReproduction()

    def traitStructure(self):
        print("Body Structure:")
        print("a. Single-celled, b. Multicellular, c. Exoskeleton, d. Endoskeleton")
        print("e. Skip")
        choice = input("Enter Your Choice: ")
        print()
        if (choice.lower() == 'a'):
            self.dictionary["Body Structure"] = "Single-celled"

        elif (choice.lower() == 'b'):
            self.dictionary["Body Structure"] = "Multicellular"

        elif (choice.lower() == 'c'):
            self.dictionary["Body Structure"] = "Exoskeleton"

        elif (choice.lower() == 'd'):
            self.dictionary["Body Structure"] = "Endoskeleton"
        
        elif (choice.lower() == 'e'):
            print("Skipped...")
        
        else:
            print("Enter Valid Choice!")
            self.traitStructure

    def traitSimilar(self):
        traits = self.dictionary.values()
        trait = []
        for what_type in traits:
            if type(what_type) == type({}):
                for key, value in what_type.items():
                    trait.extend([key,value])
            else:
                trait.append(what_type)
        
        if  'Autotrophic' in trait and 'Aquatic' in trait :
            print("Your Organsim can be similar to: Algae, Cyanobacteria")

        elif "Heterotrophic" in trait and "Terrestrial" in trait :
            print("Your Organsim can be similar to: Mammals, Birds (Predators)")
        
        elif "Lithotrophic" in trait and "Subterranean" in trait :
            print("Your Organsim can be similar to: Deep-sea Bacteria")

        elif "Aerial" in trait and "Multicellular" in trait :
            print("Your Organsim can be similar to: Bats, Birds (like Eagles)")

        elif "Parasites" in trait and "Detritivores" in trait :
            print("Your Organsim can be similar to: Tapeworms, Parasitic Fungi")
        
        elif "Exoskeleton" in trait and "Carnivores" in trait :
            print("Your Organsim can be similar to: Spiders, Scorpions")
        
        elif "Endoskeleton" in trait and "Omnivores" in trait :
            print("Your Organsim can be similar to: Humans, Bears")

        elif "Single-celled" in trait and "Lithotrophic" in trait :
            print("Your Organsim can be similar to: Sulfur Bacteria, Archaea")
        
        elif "Multicellular" in trait and "Detritivores" in trait :
            print("Your Organsim can be similar to: Sulfur Bacteria, Archaea")
        
        elif "Exoskeleton" in trait and "Omnivores" in trait :
            print("Your Organsim can be similar to: Crabs, Cockroaches")
        
        else:
            print("No Similar Organism Found")

        
    def display(self):
        print()
        print("______Your Selected Traits______\n")
        l = []
        data = self.dictionary.items()
        for catagory, ch in data:
            print(catagory, end = ": ")
            if (type(ch) != type({1:2})):
                l.append(catagory+": "+ch+"\n")
                print(ch)
            else:
                for subCat, subCatName in ch.items():
                    l.append(catagory+": "+subCat+" -> "+subCatName+"\n")
                    print(subCat,"->",subCatName)
            
        print()
        return l
    
    def callingAllFunction(self):
        self.traitNutrient()
        self.traitAmmonia()
        self.traitHabitat()
        self.traitReproduction()
        self.traitStructure()
        self.traitSimilar()

        
        
        
#_main_
obj = TraitSelection()
ch = -1
while True:
    print("1. To Know about the details of the different type of organism \n2. To play the game, 3. Name the Organism and Quit, 4. To Quit")
    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        obj.traitDetails()
    
    elif ch == 2:
        obj.callingAllFunction()
    
    elif ch == 3:
        break

    elif ch == 4:
        obj.display()
        print("Game Ended...")
        exit(0)
    
    else:
        print("Enter the Valid Choice!")


data = obj.display()
if data != []:
    orgName = input("Enter the name of your Organism: ")
    data.insert(0,"Organism Name: "+orgName+"\n")
    with open("NewOrganism.txt", 'w') as file:
        file.writelines(data)
    print("Game Ended...")
else:
    print("No Traits Selected...")
    
    print("Game Ended...")