## 1. Flowchart Diagram (T)

Evidentiaza activitatea unui user, trecand prin toate starile aplicatiei.

![](./Diagrams/Flowchart.png)

## 2. Database Diagram (F)

Exemplifica campurile si cheile tabelelor din baza de date si relatiile dintre ele.

![](./Diagrams/Db.png)

## 3. Use case Diagram (F)

Diagrama a actiunilor posibile, din perspectiva unui user autentificat dar si unuia neautentificat.

![](./Diagrams/use_case.png)

## 4. Class diagram (M)

Sunt prezentate clasele folosite pentru a construi aplicatia, continand datele membre si metodele fiecareia.

```mermaid
%%{init: {'theme':'neutral'}}%%
classDiagram
    class Movie {
        -String id
        +Enum genre
        +Int releaseYear
        +String imageUrl
        +String title
        +String[] Actors
    }
    class Review {
        -String id
        -String userId
        -String movieId
        +Int rating[1..10]
        +String reviewText
    }
  class Wishlist{
    -Int id
    -Movie movies[]
    +addMovie()
    +removeMovie()
}
class Library{
    -Int id
    -Movie movies[]
    +addMovie()
    +removeMovie()
    }
class User{
    -String id
    -String username
    -String password
    +Wishlist wishlist
    +Library library
    +login()
    +shareLibrary()
    +changePassword(newPassword)
    -sendConfirmationEmail()
    -getRecommendation()
    +addReview(movieId, rating, message)
}




Wishlist <-- Movie : contains
Library <-- Movie : contains
User *-- Wishlist : has
User *-- Library : has
Review o-- User : give
Review o-- Movie : to
```

## Diagrame de interactiune

### 5. Inregistrarea unui utilizator (M)

Exemplifica interactiunea dintre Frontend, Backend, Database si email-ul utilizatorului, prin flow-ul unui request de inregistrare.

```mermaid
sequenceDiagram
    participant Frontend
    participant Backend
    participant Database
    participant Email

    Frontend ->> Backend: Request for registering the new user
    activate Backend
    Backend ->> Email: Sending an email to the user
    activate Email
    Email ->> Backend: Accepting the invitation
    deactivate Email
    Backend ->> Database: Save user in DB
    Backend ->> Frontend: User account created
    deactivate Backend

    Frontend ->> Backend: Request for login the user
    activate Backend
    Backend ->> Database: Request the user in db
    activate Database
    Database ->> Backend: Accept/Deny user login
    deactivate Database
    Backend ->> Frontend: Login accepted or failed
    deactivate Backend
```

<br>

### 6. Obtinere a filmelor (R)

Interactiunea dintre Frontend, Backend, Database si API-ul care ne furnizeaza lista filmelor, atunci cand utilizatorul adauga un film in wishlist.

```mermaid
sequenceDiagram
    participant Frontend
    participant Backend
    participant Database
    participant PublicAPI

    Frontend ->> Backend: Request for Movie List
    activate Backend
    Backend ->> PublicAPI: Fetch Movie List
    activate PublicAPI
    PublicAPI -->> Backend: Movie List
    deactivate PublicAPI
    Backend -->> Frontend: Movie List Response
    deactivate Backend

    activate Frontend
    Frontend -->> Backend: Add movie to wishlist
    activate Backend
    Backend ->> Database: Store Wishlist
    activate Database
    Backend ->> Database: <<add>>
    Database -->> Backend: New wishlist returned
    deactivate Database
    Backend -->> Frontend: Wishlist Response
    deactivate Backend

```

## Diagrame de pachete

### 7. Backend (A)

Prezinta pachetele utilizate in backend si relatiile dintre ele.

![](./Diagrams/BackendPackageDiagram.png)

### 8. Frontend (A)

Prezinta pachetele utilizate in frontend si relatiile dintre ele.

![](./Diagrams/FrontendPackageDiagram.png)

## 9. Diagrame de stare (R)

Prezinta un state machine a paginii de cautare a unui film. Utilizatorul cauta un film dupa titlu, vede cate 10 filme pe fiecare pagina, poate sa treaca la pagina urmatoare si poate interactiona cu fiecare film in parte.

![](./Diagrams/statediagram.jpg)
