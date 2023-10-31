from time import sleep

guesses = 0
countries = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros", "Ivory Coast", "Djibouti", "Democratic Republic of the Congo", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho",
             "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Republic of the Congo", "Rwanda", "Sao Tome & Principe", "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]

countriesGuessed = []  # This stores all the countries which the user guessed

print("\nYou have to guess {0} countries from Africa.".format(
    len(countries)), "Good luck", sep="\n")

sleep(5)


def guess():
    # Get user input
    answer = input("Please enter a country: ").capitalize()

    # Check if country exists in array
    if answer in countries: 
        # Remove country from countries
        countries.remove(answer)

        # Add to countries guessed
        countriesGuessed.append(answer)

        # Tell user how many they guessed so far
        print("Your where correct; {0} is a country in Africa, now there is {1} countries left to guess.".format(
            answer, len(countries)))
        
        guess()
    
            # Check if already guessed
    if (countriesGuessed.count(answer) == 1):
        print("You already guessed {0}.".format(answer))
        guess()

    # Else not a country in africa, try again
    print("Sorry, that is not a country in Africa")
    guess()

guess()
