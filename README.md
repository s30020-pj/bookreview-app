# Oto prosta aplikacja umożliwająca przeglądanie i dodawanie książek
  Aby korzystać z opcji dodawania recenzji i/lub książek należy zalogować się w panelu administracyjnym dostępnym pod adresem http://127.0.0.1:8000/admin/
  - login: admin
  - hasło: admin

## Done:
- Lista książek
  - filtrowanie po kategoriach
  - widoczny tytuł, autor, krótki opis i średnia ocena
  - paginacja (6 na stronę)
  - wyszukiwanie książki po tytule/autorze
- Szczegóły książki
  - pełne informacje o książce
  - lista recenzji użytkowników wraz z ocenami
  - paginacja recenzji (4 na stronę)
  - dodawanie recenzji dla zalogowanych użytkowników
  - dodawanie recenzji i zmiana średniej oceny bez przeładowania strony
- Dodawanie nowej książki
  - formularz umożliwiający dodanie nowej książki
  - dostęp do formularza jedynie dla zalogowanych użytkowników
- Responsywny interfejs stworzony przy użyciu Bootstrapa
 
## ToDo
- Jest bug gdzie można dodać recenzję z inną oceną niż między 1 a 5
- Brak strony do logowania i/lub rejestracji poza panelem admina
- Brak testów

## Dodatkowe informacje
Tyle udało mi się osiągnąć w dwa dni, bez wcześniejszego doświadczenia z frameworkiem. Jestem świadomy że nie jest to najlepsza aplikacja i brakuje mi jeszcze wielu dobrych praktyk, ale z moją zdolnością szybkiego uczenia się jestem w stanie szybko te braki nadrobić
