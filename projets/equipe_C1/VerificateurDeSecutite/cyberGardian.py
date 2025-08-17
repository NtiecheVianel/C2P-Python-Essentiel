print("🔐 === CYBERGUARDIAN : TESTEZ VOTRE SÉCURITÉ NUMÉRIQUE ! ===\n")
print("Bienvenue ! Ce quiz va évaluer vos habitudes de cybersécurité.")
score = 0
print("Répondez par 'oui' ou 'non' à chaque question.\n")
a = input("Question 1/5: Utilisez-vous un mot de passe différent pour chaque compte ?")
if a == "oui":
     score += 1
b = input("Question 2/5: Vérifiez-vous l'URL avant de saisir vos informations personnelles ?")
if b == "oui":
     score += 1
c = input("Question 3/5: Activez-vous les mises à jour automatiques de sécurité ?")
if c == "oui":
     score += 1
d = input("Question 4/5: Évitez-vous de vous connecter sur des réseaux Wi-Fi publics pour des tâches sensibles ?")
if d == "oui":
     score += 1
e = input("Question 5/5: Utilisez-vous l'authentification à deux facteurs quand c'est possible ?")
if e == "oui":
     score += 1
print()

    # Analyse des résultats
print("🎯 === VOTRE PROFIL CYBERSÉCURITÉ ===\n")

if score >= 4:
    print("🟦 CYBER-EXPERT")
    print("Excellent niveau de sécurité, continuez ainsi !")
elif 2 <= score <= 3:
    print("🟧 UTILISATEUR PRUDENT")
    print("Vous avez de bonnes bases mais quelques améliorations sont possibles !")
else:
    print("🟥 CYBER-NOVICE")
    print("Attention, des améliorations sont nécessaires pour renforcer votre sécurité numérique.")

    # Conseils personnalisés
    print("\n💡 Conseils personnalisés :")
    if a == "non":
        print("- Pensez à utiliser un gestionnaire de mots de passe.")
    if d == "non":
        print("- Méfiez-vous des réseaux Wi-Fi publics pour vos comptes importants.")
    if e == "non":
        print("- Activez l’authentification à deux facteurs pour plus de sécurité.")

print(f"\nScore final : {score}/5 – Merci d’avoir participé au quiz !")
