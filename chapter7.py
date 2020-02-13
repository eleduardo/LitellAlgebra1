def prompt_for_numeric(prompt: str):
    while 1:
        value = input(prompt + ' --> ')
        if not value or not value.isnumeric():
            print("I need numeric value without symbols")
        else:
            break
    return value


def main():
    dash = '-' * 40
    print('Welcome to the Chapter 7 exercise: Applying fractions')
    print("Let's calculate interests!!")
    initial = prompt_for_numeric('Enter the initial amount to invest')
    interest = prompt_for_numeric('Enter the interest earned as percentage')
    years = prompt_for_numeric('Enter the number of years to calculate')
    print('Calculating for ' + years + ' years ')
    print(dash)
    print('{:<10s}{:>4s}{:>12s}'.format('Year', 'Initial', 'Final'))
    print(dash)
    interest_fraction = float(interest)/100
    acumulator = float(initial)
    for year in range(1, int(years)+1):
        final = acumulator + acumulator * interest_fraction
        print('{:<10d}{:>4.2f}{:>12.2f}'.format(year, acumulator, final))
        acumulator = final


if __name__ == "__main__":
    main()
