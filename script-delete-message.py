import pyautogui
import time
import pyperclip  # Pour copier le texte dans le presse-papiers


# Fonction pour faire défiler la conversation
def scroll_conversation(scrolls=10, delay=1):
    for _ in range(scrolls):
        pyautogui.scroll(300)  # Faites défiler vers le haut plus rapidement
        time.sleep(delay)


# Fonction pour capturer le texte affiché à l'écran
def capture_messages():
    # Copiez tout le texte affiché à l'écran dans le presse-papiers
    pyautogui.hotkey('ctrl', 'a')  # Sélectionnez tout
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')  # Copiez
    time.sleep(0.5)
    messages = pyperclip.paste()  # Collez le texte du presse-papiers
    return messages


# Fonction pour identifier les messages envoyés par différentes personnes et les imprimer
def identify_and_print_messages(messages):
    lines = messages.split('\n')
    sender = None
    for line in lines:
        if line.endswith(':'):
            sender = line.strip(':')
        elif line:
            if sender:
                if sender in ['Vous', 'You']:
                    print(f"Message envoyé par vous (à supprimer): {line.strip()}")
                    delete_message(line.strip())
                else:
                    print(f"Message de {sender}: {line.strip()}")
            else:
                print(f"Autre message ou information: {line.strip()}")


# Fonction pour supprimer un message
def delete_message(message_text):
    try:
        # Rechercher et cliquer sur le message pour afficher les options
        pyautogui.click(
            pyautogui.locateCenterOnScreen('message_icon.png'))  # Remplacez par l'icône spécifique si nécessaire
        time.sleep(1)

        # Sélectionner l'option de suppression
        pyautogui.click(
            pyautogui.locateCenterOnScreen('delete_option.png'))  # Remplacez par l'icône de suppression si nécessaire
        time.sleep(1)

        # Confirmer la suppression
        pyautogui.click(pyautogui.locateCenterOnScreen(
            'confirm_delete.png'))  # Remplacez par le bouton de confirmation de suppression
        time.sleep(1)

        print(f"Message supprimé: {message_text}")
    except Exception as e:
        print(f"Erreur lors de la suppression du message: {e}")


# Fonction principale pour défiler et capturer les messages en continu
def main():
    # Attendez que vous ayez ouvert l'application Messenger et sélectionné une conversation
    time.sleep(5)

    previous_messages = set()
    while True:
        scroll_conversation()
        messages = capture_messages()
        new_messages = set(messages.split('\n')) - previous_messages
        previous_messages.update(new_messages)

        for message in new_messages:
            identify_and_print_messages(message)

        time.sleep(1)  # Ajoutez un délai court pour accélérer le processus


# Exécution du script
if __name__ == "__main__":
    main()
