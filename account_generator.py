import random
import string
import time
import sys
import os

syllables = ["ka", "mi", "zo", "li", "ra", "na", "tu", "ja", "ka", "ri", "mo", "sa", "ta", "ni", "da", "la", "va"]

def generate_username(length=3):
    return ''.join(random.choice(syllables) for _ in range(length)).capitalize()

def generate_email(username, domains):
    return f"{username.lower()}@{random.choice(domains)}"

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def print_progress_bar(iteration, total, length=40):
    percent = (iteration / total) * 100
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r|{bar}| {percent:.2f}% Complété')
    sys.stdout.flush()

def generate_accounts(num_accounts, username_length, email_domains, password_length):
    with open("accounts.txt", "w") as file:
        for i in range(num_accounts):
            username = generate_username(username_length)
            email = generate_email(username, email_domains)
            password = generate_password(password_length)
            file.write(f"Nom d'utilisateur : {username}\n")
            file.write(f"E-mail : {email}\n")
            file.write(f"Mot de passe : {password}\n")
            file.write("\n")
            print_progress_bar(i + 1, num_accounts)
            time.sleep(0.05)

    print(f"\n\n{num_accounts} comptes générés et enregistrés dans 'accounts.txt'.")

def display_accounts():
    if not os.path.exists("accounts.txt"):
        print("Aucun compte trouvé. Veuillez d'abord générer des comptes.")
        return

    with open("accounts.txt", "r") as file:
        accounts = file.read()
        print("\n--- Comptes générés ---\n")
        print(accounts)

def main():
    print("Bienvenue dans le générateur d'idées de comptes !")
    while True:
        print("\n--- Menu ---")
        print()
        print("1. Générer des comptes (nom d'utilisateur, e-mail, mot de passe)")
        print()
        print("2. Afficher les comptes existants")
        print()
        print("3. Quitter")
        print()

        choice = input("Choisissez une option (1-3) : ")

        if choice == '1':
            num_accounts = int(input("\nEntrez le nombre de comptes à générer : "))
            username_length = int(input("\nEntrez le nombre de syllabes pour le nom d'utilisateur (2-4) : "))
            email_choice = input("\nVoulez-vous utiliser un domaine spécifique (gmail, yahoo, hotmail, outlook) ? (o/n) : ").strip().lower()

            if email_choice == 'o':
                email_domains = input("\nEntrez les domaines séparés par des virgules (ex: gmail.com,yahoo.com) : ").split(',')
                email_domains = [domain.strip() for domain in email_domains]
            else:
                email_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]

            password_length = int(input("\nEntrez la longueur souhaitée pour le mot de passe : "))

            if num_accounts <= 0 or username_length < 2 or username_length > 4 or password_length <= 0:
                print("Veuillez entrer des nombres valides.")
                continue
            
            generate_accounts(num_accounts, username_length, email_domains, password_length)

        elif choice == '2':
            display_accounts()

        elif choice == '3':
            print("Au revoir !")
            break

        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
