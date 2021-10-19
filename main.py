import classes
import os
from utils import print_statistics


def guidelines():
    """
                                    /$$      /$$
                                   | $$     | $$
  /$$$$$$$ /$$$$$$$ /$$$$$$ /$$$$$$| $$$$$$$| $$ /$$$$$$
 /$$_____//$$_____//$$__  $|____  $| $$__  $| $$/$$__  $$
|  $$$$$$| $$     | $$  \__//$$$$$$| $$  \ $| $| $$$$$$$$
 \____  $| $$     | $$     /$$__  $| $$  | $| $| $$_____/
 /$$$$$$$|  $$$$$$| $$    |  $$$$$$| $$$$$$$| $|  $$$$$$$
|_______/ \_______|__/     \_______|_______/|__/\_______/

        Το συγκεκριμένο πρόγραμμα υλοποιεί μια παραλλαγή του παιχνιδιού scrabble, όπως αυτό ζητήθηκε στην άσκηση.
    Η δομή της εργασίας είναι η παρακάτω:
    scrable/
        ├── classes.py: Το όποιο περιέχει τις κλάσεις που κατασκευάστηκαν/
        ├── greek7.txt: Το δοσμένο αρχείο με τις λέξεις τις ελληνικής μέχρι 7 χαρακτήρες/
        ├── main-AEM.py: Το αρχείο κώδικα που περιέχει την κύρια συνάρτηση του προγράμματος (main)/
        ├── results.json: Το αρχείο json με τα αποτελέσματα - στατιστικά των παιχνιδιών/
        └── utils.py: ένα αρχείο κώδικα με ορισμένες βοηθητικές συναρτήσεις για την εκτέλεση του κώδικα όπως συναρτήσεις για το διάβασμα-γράψιμο json κ.α./

    Για την υλοποίηση του παιχνιδιού έχουμε αναπτύξει τις εξής κλάσεις (οι όποιες περιέχονται στο αρχείο classes.py):
    1. SakClass: Η οποία ουσιαστικά προσομοιώνει την λειτουργία που έχει το σακουλάκι στο φυσικό παιχνίδι. Η κλάση αυτή έχει μια λίστα την όποια ονομάζει sak
                 η όποια κρατάει όλα τα γράμματα που υπάρχουν στο παιχνίδι, όπως ακριβώς στο πραγματικό παιχνίδι. Αφού κατασκευάσουμε την λίστα αυτή με όλα τα γράμματα στην συνέχεια την ανακατεύουμε ώστε τα γράμματα να τοποθετηθούν σε τυχαίες θέσεις μέσα στο σακουλάκι!
                 Έτσι όταν ο παίχτης 'τραβάει' ορισμένα γράμματα τότε
                 η κλάση αυτή είναι υπεύθυνη να σβήσει και τα συγκεκριμένα γράμματα από την λίστα sak, όπως ακριβώς αφαιρούνται και από το σακουλάκι στο πραγματικό παιχνίδι.
                 Επίσης μπορούμε να προσθέσουμε-επιστρέψουμε γράμματα στο σακουλάκι, πράγμα το όποιο γίνεται για παράδειγμα όταν ο παίχτης πάει πάσο. Έτσι όταν γίνει αυτό
                 τα αντίστοιχα γράμματα επαναπροστίθενται στην λίστα sak έτσι ώστε να είναι δυνατά να επιλεγούν από τον επόμενο παίχτη. Οι μέθοδοι τις κλάσης είναι οι: __init__, __repr__,
                    ➼randomize_sak: η όποια επιλέγει τυχαία γράμματα από το σακουλάκι (αλλά δεν τα αφαιρεί από το σακουλάκι).
                    ➼getletters: η όποια επιστρέφει μερικά τυχαία γράμματα στον παίχτη (βγάζοντας τα από το σακουλάκι). Η συγκεκριμένη μέθοδος χρησιμοποιεί την randomize_sak για να επιλέξει γράμματα και στην συνέχεια
                                αυτά τα επιστρέφει στον παίχτη.
                    ➼putbackletters: Η οποία δέχεται σαν είσοδο μια λίστα γραμμάτων και επιστρέφει και τα ξαναβάζει στο σακουλάκι (στην περίπτωση πάσου του παίχτη χρησιμοποιείται).
                    ➼saksize: Η συγκεκριμένη μέθοδος επιστρέφει τον αριθμό των γραμμάτων που έχουν απομείνει στο σακουλάκι.
    2. Rack: Η όποια δεν ζητήθηκε αλλά την υλοποίησα εγώ μιας και την θεώρησα χρήσιμη για την κατανόηση των βημάτων του αλγορίθμου. Η μέρος αυτή ουσιαστικά υλοποιεί
             την λειτουργία του δίσκου πάνω στον όποιον τοποθετούνται τα πλακίδια με τα γράμματα. Η μέθοδος αυτή ουσιαστικά έχει μια λίστα 7 θέσεων στην όποια είτε θα υπάρχει
             ένα γράμμα είτε θα είναι None - κενό πράγμα που σημαίνει ότι θα η συγκεκριμένη θέση θα είναι κενή. Η κλάση αυτή έχει τις παρακάτω μεθόδους:
                ➼__init__: Η όποια αρχικοποιεί το δίσκο με κενό
                ➼__repr__: Η όποια τυπώνει το περιεχόμενο του δίσκου, δηλαδή τα γράμματα τα όποια είναι τοποθετημένα σε αυτόν
                ➼add_tiles: Που δέχεται μια λίστα από γράμματα και τα τοποθετεί στις κενές- None θέσεις του δίσκου. Υλοποιήσαμε γενικά την μέθοδο αυτή ώστε
                                 τα νέα γράμματα που μπαίνουν στον δίσκο να μπαίνουν στις θέσεις των παλιών και αυτό ακριβώς κάνει και η συγκεκριμένη μέθοδος.
                                 Αυτό το κάναμε γιατί ύστερα από την επαφή μας με το παιχνίδι είδαμε ότι είναι πολύ πιο εύκολο στην ροή και στην κατανόηση του παιχνιδιού,
                                 τα νέα γράμματα του παίχτη να τοποθετούνται στις θέσεις των παλαιών αντί π.χ. στην αρχή ή στο τέλος. Με αυτόν τον τρόπο ο χρήστης καταλαβαίνει καλύτερα τα
                                 γράμματα που μπήκαν πως μπορούν να συνδυαστούν με τα παλιά κ.α. Στην ουσία η λειτουργικότητα αυτή βελτιώνει κατά πολύ την λειτουργικότητα του παιχνιδιού από πλευρά gui.
                ➼remove_tiles: Δέχεται μια λίστα από γράμματα και τα αφαιρεί από τον δίσκο, βάζοντας στην αντίστοιχη θέση των πλακιδίων None.
                ➼rollback: Αναιρεί την τελευταία εισαγωγή, δηλαδή βγάζει τα πλακίδια που μπήκαν τελευταία και τα επιστρέφει πίσω (ώστε να μπορεί στην συνέχεια να τα προσθέσουμε στο σακουλάκι).
                            Για να μπορούμε να το κάνουμε αυτό αποθηκεύουμε σε κάθε εισαγωγή σε μια μεταβλητή last_lets τα τελευταία γράμματα που εισαγάγαμε στον δίσκο.
    3.Requlator: Η όποια δεν ζητήθηκε αλλά την υλοποίησα για να είναι το κυρίως πρόγραμμα ευκολότερα κατανοητό και ουσιαστικά προσομοιώνει την λειτουργία ενός
                 διαιτητή στον πραγματικό κόσμο. Η μέθοδος αυτή γνωρίζει όλες τις λέξεις (από το αρχείο greek7.txt), και γνωρίζει και τους κανονισμούς σχετικά με
                 το πότε μια λέξη είναι αποδεκτή, ποιο είναι το σκορ της κ.α.
                 Η συγκεκριμένη κλάση, διαβάζει το αρχείο greek7.txt και αποθηκεύει τις λέξεις σε ένα ΛΕΞΙΚΌ (dictionary-set) και όχι σε μια λίστα για λόγους απόδοσης.
                 Συγκεκριμένα αν είχαμε αποθηκεύσει τις λέξεις σε μια λίστα τότε για να δούμε αν μια λέξη που εισήγαγε ο χρήστης είναι αποδεκτή θα έπρεπε να ψάξουμε γραμμικά
                 ολόκληρη της λίστα πράξη πολυπλοκότητας: Ο(N), όπου Ν ο αριθμός των λέξεων στο αρχείο greek7.txt.
                 Από την άλλη η ίδια πράξη (αναζήτησης) σε ένα dictionary έχει πολυπλοκότητα: Θ(1) (λόγω ότι στην Python η δομή αυτή ουσιαστικά είναι ένα hashtable), δηλαδή στην μέση περίπτωση μια πράξη! Αυτό καθιστά το πρόγραμμα μας πολύ
                 πιο γρήγορο από να χρησιμοποιούσαμε λίστα! Το κόστος της λίστας θα ήταν πολύ πιο έντονο όταν θα δοκιμάζαμε όλες τις λέξεις του υπολογιστή αν υπάρχουν στην λίστα, πράγμα που θα μπορούσε
                 να κάνει τον αλγόριθμο του υπολογιστή αδύνατο να τρέξει σε πραγματικό χρόνο.
                 Η συγκεκριμένη κλάση έχει τις εξής μεθόδους:
                    ➼__init__: Η όποια διαβάζει το αρχείο greek7.txt και αποθηκεύει όλες τις λέξεις σε ένα dictionary
                    ➼checkword: Η όποια δέχεται σαν είσοδο μια λίστα με τα γράμματα του χρήστη μαζί με μια λέξη και επιστρέφει το σκορ της λέξης μαζί με ένα μήνυμα για τον χρήστη.
                                 Αν η λέξη δεν είναι έγκυρη επιστρέφει σαν σκορ 0 αλλά το μήνυμα είναι αντιπροσωπευτικό του λόγου για τον όποιόν η λέξη δεν είναι αποδεκτή
                                 π.χ. δεν ανήκει στο σύνολο των αποδεκτών λέξεων ή τα γράμματα και η λέξη δεν ταιριάζουν κ.α.
    4. Player: Η όποια ουσιαστικά αποτελεί την βασική μέθοδο από την όποια κληρονομούν οι παίχτες, δηλαδή ο άνθρωπος και ο υπολογιστής.
    5. Human: Η κλάση η όποια κληρονομεί από την Player και ουσιαστικά προσομοιώνει τον παίχτη. Η κλάση αυτή έχει ένα δίσκο (rack) επάνω στο όποιο τοποθετεί τα γράμματα
              καθώς και την μέθοδο play η όποια προσομοιώνει την παρτίδα του παίχτη! Έτσι η συνάρτηση αυτή αρχικά τυπώνει στον χρήστη τα περιεχόμενα του πλακιδίου του και στην συνέχεια
              διαβάζει την λέξη του χρήστη. Αρχικά η λέξη αυτή συγκρίνεται με το p που δηλώνει το πάσο και το q που είναι η παραίτηση του παίχτη. Αν ο παίχτης πατήσει q
              τότε η συνάρτηση επιστρέφει και επικοινωνεί στην μέθοδο που την κάλεσε ότι ο παίχτης παραιτήθηκε. Αν ο παίχτης δώσει μια λέξη τότε αυτή ελέγχεται από τον
              ρυθμιστή-διαιτητή του παιχνιδιού ως προς την εγκυρότητά της. Αν είναι έγκυρη τότε τα γράμματα τις λέξης αφαιρούνται από το δίσκο του παίχτη, και επιλέγονται νέα
              για να τοποθετηθούν (τα γράμματα που χρησιμοποίησε ο παίχτης προφανώς δεν επιστρέφονται στο σακουλάκι αλλά θεωρητικά τοποθετούνται σε κάποιο table, αλλά η παραλλαγή μας δεν έχει κάτι τέτοιο).
              Στην συνέχεια στο σκορ του παίχτη προστίθεται και το σκορ της συγκεκριμένης λέξης! Αν ο χρήστης πάει πάσο τότε από τον δίσκο του παίχτη γίνεται ένα rollback,
              δηλαδή αφαιρούνται τα γράμματα που τοποθετήθηκαν τελευταία, επιλέγονται νέα για τις θέσεις αυτές και στην συνέχεια αφού επιλεχθούν τα παλιά επανατοποθετούνται στο σακουλάκι, όπως ακριβώς αναφέρεται και στις διαφάνειες-εκφώνησης της εργασίας
              Αξίζει να σημειωθεί ότι η συνάρτηση play επιστρέφει και έναν κωδικό επικοινωνίας σχετικά με το αν η κίνηση του χρήστη ολοκληρώθηκε με επιτυχία ή όχι.
              Έτσι αν η κίνηση του χρήστη ολοκληρώθηκε επιτυχημένα (δηλαδή έβαλε μια έγκυρη λέξη ή πήγε πάσο) τότε επιστρέφεται ο κωδικός 0, ενώ αν πατήσει q, δηλαδή επιθυμεί να τελειώσει
              το παιχνίδι επιστρέφεται -1.

    6. Computer: Η κλάση η όποια κληρονομεί από την Player και ουσιαστικά προσομοιώνει τον υπολογιστή. Η κλάση αυτή έχει ένα δίσκο (rack) επάνω στο όποιο τοποθετεί τα γράμματα ο παίχτης - Υπολογιστής
              καθώς και την μέθοδο play η όποια προσομοιώνει την παρτίδα του υπολογιστή! Όπως και η αντίστοιχη συνάρτηση του Human αρχικά τυπώνει τα γράμματα που έχει ο παίχτη-Υπολογιστής στο δίσκο του και στην συνέχεια
              αντί να περιμένει την κίνηση του παίχτη - ανθρώπου, υπολογίζει την λέξη που θα παίξει σύμφωνα με το Σενάριο 1, δηλαδή έχουμε υλοποιήσει 3 αλγορίθμους τον max, min και τον smart. Η επιλογή του αλγορίθμου γίνεται από τις ρυθμίσεις του παιχνιδιού
              ενώ η default επιλογή είναι η smart. Οι 2 πρώτοι αλγόριθμοί (Min, Max) ουσιαστικά είναι ίδιοι μεταξύ τους με την μόνη διαφορά τους να έγκειται στο αν ορίζουμε να παράγουμε λέξεις με 2 γράμματα και στην συνέχεια αυξάνουμε μέχρι το 7 ή το αντίθετο.
              Σε όποια από τις 2 περιπτώσεις στην πρώτη έγκυρη λέξη που θα συναντήσουμε θα σταματήσουμε το ψάξιμο και δώσουμε την συγκεκριμένη λέξη ως απάντηση του υπολογιστή.
              Αυτή η κλάση συνεπώς έχει και τις 3 μεθόδους για την λειτουργία του αλγορίθμου τις: min_algorithm, max_algorithm, smart_algorithm. Τέλος αξίζει να σημειωθεί
              ότι όπως η μέθοδος run της κλάσης Human έτσι και η αντίστοιχη μέθοδος εδώ στο τέλος της εκτέλεσής της επιστρέφει σε αυτόν που την κάλεσε ένα κωδικό επικοινωνίας
              για το αν η κίνηση ολοκληρώθηκε με επιτυχία ή προέκυψε κάποιο σφάλμα!
              Στην αρχική υλοποίηση της άσκησης ο υπολογιστής είχε την δυνατότητα αν δεν βρει μια λέξη να μπορεί να πάει πάσο και να αλλάξει τα τελευταία του γράμματα όπως ακριβώς μπορεί να κάνει και ο χρήστη.
              Παρόλα αυτά η εκφώνηση ζητούσε όταν ο υπολογιστής δεν μπορεί να βρει μια λέξη τελειώνει η παρτίδα και αυτό είναι που υλοποιήσαμε και εδώ τελικά.
              Έτσι αν για τα γράμματά του ο υπολογιστής δεν καταφέρει να βρει καμία λέξη τότε επιστρέφει κωδικό λάθους στον κώδικα που την κάλεσε (την play) και η παρτίδα στην συνέχεια λήγει.

    7. Game: Η συγκεκριμένη κλάση είναι υπεύθυνη για την σωστή διεξαγωγή του παιχνιδιού (όχι των ρυθμίσεων ή των σκορ μιας και αυτό το αναλαμβάνει ο κώδικα της main) αλλά για τις παρτίδες,
             το σωστό σταμάτημα του παιχνιδιού κ.α. Η κλάση αυτή έχει τις παρακάτω μεθόδους:
                ➼__init__: Η συγκεκριμένη μέθοδος είναι υπεύθυνη για να αποθηκεύσει στην μνήμη της μερικές παραμέτρους του παιχνιδιού, όπως το αλγόριθμο που θα παίζει ο υπολογιστής και το όνομα
                            του αρχείου στο όποιο θα αποθηκεύονται τα δεδομένα-στατιστικά του παιχνιδιού, ώστε να μπορεί να αποθηκεύει τις αντίστοιχες πληροφορίες στο τέλος του.
                ➼__repr__: Η συγκεκριμένη μέθοδος είναι υπεύθυνη για να επιστρέφει ένα βασικό str του κάθε στιγμιότυπου παιχνιδιού.
                ➼setup: Η συγκεκριμένη μέθοδος είναι υπεύθυνη για την δημιουργία του παιχνιδιού ώστε να μπορεί να ξεκινήσει! Για να μπορεί να γίνει αυτό η συγκεκριμένη μέθοδος πρέπει να κατασκευάσει
                         ένα στιγμιότυπο της κλάσης παίχτης - Άνθρωπος και ένα στιγμιότυπο της κλάσης παίχτης - Υπολογιστής. Επίσης πρέπει να κατασκευάσει και ένα στιγμιότυπο της κλάσης διαιτητής ο
                         όποια θα είναι υπεύθυνος για τον έλεγχο των λέξεων που εισάγονται καθώς και ένα σακουλάκι με τα γράμματα!
                ➼run: Η μέθοδος αυτή είναι υπεύθυνη για την διεξαγωγή του παιχνιδιού. Κάθε φορά καλεί να παίξει είτε ο παίχτης - Άνθρωπος είτε ο παίχτης - υπολογιστής και ελέγχει τον κωδικό
                       που επιστρέφουν. Αν κάποια από τις 2 συναρτήσεις επιστρέψει κωδικό λάθους -1, τότε το παιχνίδι λήγει και καλείται η μέθοδος end της ίδιας κλάσης η όποια έχει ως σκοπό να αποθηκεύσει
                       τα αποτελέσματα που παιχνιδιού στο αρχείο filename που δόθηκε.
                ➼end: Η συγκεκριμένη μέθοδος έχει ως σκοπό να λήξει το παιχνίδι, αρχικά επιστρέφοντας το κατάλληλο μήνυμα στον χρήστη για τον νικητή και τους πόντους του και στην συνέχεια για να αποθηκεύσει τα
                       αποτελέσματα του παιχνιδιού στο αρχείο json. Αν το αρχείο υπάρχει ήδη τότε προσθέτει τα αποτελέσματα του συγκεκριμένου παιχνιδιού σε αυτό μαζί με τα άλλα, αλλιώς αρχικά δημιουργεί το αρχείο και στην συνέχεια αποθηκεύει τα αντίστοιχα δεδομένα.
    """
    pass

if __name__=="__main__":

    # Αρχίζει η εκτέλεση του παιχνιδιού με πρώτο βήμα την εμφάνιση των επιλογών του χρήστη
    computer_method = "smart" # η default μέθοδος που θα  τρέχει ο αλγόριθμος του υπολογιστή
    filename = "results.json" # το αρχείο με τα δεδομένα του προγράμματος


    while (True): # μέχρι να γίνει κάτι και να βγούμε από την λούπα (θα γίνει π.χ. όταν πατήσουμε q)
        # εμφανίζουμε ένα μήνυμα στον χρήστη με τις επιλογές του
        print ("************************* SCRABLE ************************")
        print ("----------------------------------------------------------")
        print ("1. Σκορ")
        print ("2. Ρυθμίσεις")
        print ("3. Παιχνίδι")
        print ("q. Έξοδος")
        print ("----------------------------------------------------------")
        option = input('Εισήγαγε μια επιλογή: ', )

        # με δεδομένη την επιλογή του χρήστη θα κάνουμε ένα από τα παρακάτω
        if option == "1": # αν θέλει να δει το σκορ
            if os.path.exists(filename): # φορτώνουμε το αρχείο (αν υπάρχει)
                print_statistics(filename) # αν υπάρχει καλούμε την συνάρτηση για την εκτύπωση των στατιστικών η όποια βρίσκεται στο utils και περιγράφεται εκεί και η λειτουργία της
            else: # αν το αρχείο δεν υπάρχει σημαίνει ότι δεν έχει παιχθεί κανένα παιχνίδι ή σβήστηκε το αρχείο οπότε εμφανίζουμε κατάλληλο μήνυμα
                print ("Δεν υπάρχουν ακόμα δεδομένα σχετικά με τα παιχνίδια! Ξεκίνησε ένα παιχνίδι και τα στατιστικά θα αποθηκευτούν αυτόματα!")
            input("Enter για συνέχεια") # περιμένουμε τον χρήστη να πατήσει enter και ξαναμπαίνουμε στο μενού
            print ("-----------------------------------------------------------")
        elif option == "2": # στην επιλογή 2 τυπώνουμε τις ρυθμίσεις
            print ("Ρυθμίσεις: ")
            while True: # περιμένουμε από τον χρήστη να εισάγει την μέθοδο που θέλει να παίζει ο υπολογιστής
                print (f"Πληκτρολόγησε τον αλγόριθμο του υπολογιστή από το Σενάριο 1. Η τρέχουσα επιλογή είναι η: {computer_method}")
                computer_method = input ("Επιτρεπτές επιλογές: Min, Max ή Smart: ").lower() # διαβάζουμε επιλογή και την κάνουμε Lower για να μην έχουμε θέμα με το αν έχουμε κεφαλαία ή πεζά
                if computer_method in ["min", "smart", "max"]: # πρέπει η μέθοδος να είναι μια εκ των Min, max, smart, δεν μας πειράζει καθόλου το case
                    print (f"Η επιλογή σου αποθηκεύτηκε επιτυχώς! Ο αλγόριθμος του υπολογιστή για την παρτίδα είναι ο: {computer_method}")
                    input("Enter για συνέχεια") # ενημερώνουμε τον χρήστη για την αλλαγή και περιμένουμε να πατήσει Enter ώστε να ξαναμπούμε στο μενού
                    break # βγαίνουμε από τη  εσωτερική λούπα, αν δεν φτάσουμε εδώ σημαίνει ότι ο χρήστης έδωσε μια άλλη λέξη πέρα των 3 επιλογών που είχε οπότε πρέπει να ξαναεισάγει επιλογή
                else:
                    print (f"Η επιλογή {computer_method} δεν ανήκει στις επιτρεπτές! Παρακαλώ πληκτρολόγησε μια επιτρεπτή μέθοδο!")
                print ("-----------------------------------------------------------")
        elif option == "3":
            # ο αλγόριθμος της εκτέλεσης του παιχνιδιού
            game  = classes.Game(computer_method, filename) # σε αυτήν την επιλογή κατασκευάζουμε το παιχνίδι
            game.run() # και μετά ξεκινάμε
        elif option == "q":
            print ("Σε ευχαριστούμε πολύ!") # ο χρήστης αποχωρεί του τυπώνουμε κατάλληλο μήνυμα
            break
        else:
            print ("Επέλεξε μια από τις αποδεκτές επιλογές") # λάθος επιλογή πρέπει να βάλει κάτι μεταξύ το 1, 2, 3, q και όχι κάτι άλλο
