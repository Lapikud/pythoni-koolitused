Pythoni koolitus peaaegu algajatele: pigem lihtne minesweeperi mäng
===================================================

Enne koolitust
==============

+ Tee kindlaks, et arvutitel oleks mingi kindel IDE (Pearu soovitab Pycharmi)
+ Tee kindlaks, kas arvutitel on Python2 või Python3, sellest sõltub antud koolitusel sõne vormindamine:
	+ %-vormindamine on saadaval mõlemas versioonis
	+ format() funktsioon on saadaval mõlemas versioonis
	+ f-sõne vormindamine on saadaval vaid Python 3.6-s ja hilisemates versioonides.
+ Ava arvutitel tühi PyCharmi projekt ja pane töölaudadele koodispikker (näiteks siinolev juhend), et abistajatel oleks lihtsam aidata.
+ Oma arvutitega tulijate jaoks hoia mälupulgal:
	+ Python2 või Python3 paigaldajat peamise kolme OS-i jaoks
	+ Pycharmi paigaldajat peamise kolme OS-i jaoks
+ Vaadata, et projektori pilt oleks piisavalt suur ja selge
+ Läbiviija IDE-s valida menüüdest View -> Enter presentation mode, et kindlustada esitluse selgus ja hea välimus.


Algus
=====

Kõigepealt luua Minesweeperi klass koos väga algelise konstruktori ja print_map() meetodiga. Luua ka main meetod, et klassi ja instantse seletada: 

::

    class Minesweeper:
    
        def __init__(self, rows):
            self.rows = rows

        def print_map(self):
            print(self.rows)

    if __name__ == "__main__":
        sweeper = Minesweeper(4)
        sweeper.print_map()
        
        ms = Minesweeper(3)
        ms.print_map()


Täiendame konstruktorit: lisame sinna ``self.columns`` ja salvestame sinna uue parameetri väärtuse.

Nüüd kirjutame ridade ja veergude arvu põhjal maatriksi genereerimise funktsiooni:

::

    def blank_map(self):
        blank_map = []

        for row in range(self.rows):
            # Make row_list to hold all fields
            row_list = []
            for col in range(self.columns):
                # Append one field to row_list
                row_list.append("-")
            # Append row to blank_map
            blank_map.append(row_list)
        return blank_map


Prindime selle *main* meetodis välja: ``print(sweeper.blank_map())``
Lisame klassimuutuja ``self.game_map`` ja salvestame sinna .blank_map() tulemuse. 

Nüüd tekitame maatriksist kasutajasõbraliku esitusviisi, kus iga rida on eraldi real ja tulbad on kohakuti. Kuna me tahame mänguväljal kujutada ka kursori asukohta (kursoriga ümbritsetud lahter näeks välja "<->"), siis ümbritseme reas iga lahtri ühe tühikuga:
" -  -  - " oleks 1x3 kursorita mänguväli. 

**TODO: teha print_map väiksemateks tükkideks (kõigepealt ilma kursorita)**

::

    def print_map(self):
        """
        Print the user_view ~aesthetically~ and show the pointer on it.

        :return:
        """

        for i, row_list in enumerate(self.user_view):  # https://docs.python.org/3/library/functions.html#enumerate

            pointer_row, pointer_col = self.pointer_coords

            # how we want our pointer look when it's surrounding a cell:
            # <->

            # the row with the pointer has to be printed a little differently
            if i == pointer_row:

                row = []

                for j, cell in enumerate(row_list):

                    if j == pointer_col:
                        row.append(f"<{cell}>")
                    else:
                        row.append(f" {cell} ")
                print("".join(row))
            # print the normal row
            else:
                print(" " + "  ".join(row_list) + " ")                


Lisada vahepeal ``self.pointer_coords = [0, 0]``

**TODO: test out handle_input and game for best ordering**

Lisada ``def handle_input(self, move)``. *Out of bounds* kontroll lisada alles siis, kui käivitades see viga üles leitakse! handle_input() testimiseks realiseerida game().

::

    def handle_input(self, move):

        pointer_row, pointer_col = self.pointer_coords

        if move == "w":
            pointer_row -= 1
        elif move == "s":
            pointer_row += 1
        elif move == "a":
            pointer_col -= 1
        elif move == "d":
            pointer_col += 1

        self.pointer_coords = pointer_row, pointer_col

    def game(self):

        while True:
            self.print_map()
            print()
            move = input()

            self.handle_input(move)


Peale käivitamist võiks märgata, et me ei keela kursoriga üle mänguväljaku ääre liikumist. Defineerime selle jaoks funktsiooni:

::

    def in_bounds(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.columns

Kasutame seda funktsiooni ``handle_input`` funktsiooni lõpus:

::

        if self.in_bounds(pointer_row, pointer_col):
            self.pointer_coords = pointer_row, pointer_col

Infota mänguväli ja sellel kursoriga liikumine on realiseeritud. Järgmiseks tuleb tekitada infoga mänguväli, st arvutile teadaolev informatsioon.
See mänguväli koosneb miinidest ("*"), miinide kõrvalväljadest (tähistuseks on stringi kujul täisarv, mis vastab lahtrit ümbritsevate miinide arvule) ning tühjadest (" ") lahtritest.


**TODO: muuta blank_map, luua create_map ja miinidega seotu**


12.10.2018 jätkukoolitus
=====

Enne koolitust võiks parandada osalistel mahakirjutamisel tekkinud errorid. Kaks puudujääki jäi eelmine kord ka tahvlil olevasse koodi, neid võiks koos parandada, `järgides eelnevale koodile lisatud TODO märkmeid
<http://www.python.org/>`_. Kui juhtumisi peaks mõni uus või väga rappa läinud osaleja ette juhtuma, võib neile lihtsalt `selle koodi anda
<http://www.python.org/>`_.

Ülevaade eelmisest koolitusest (hea mäluvärskendus ka osalejatele!):
Loodi minesweeperi klass. Klassiomaduste hulgas on mänguvälja mõõtmed, miinide arv, kursori asukoht ja arvutile teadaolev mänguvali (ehk lõpus avalduv mänguväli).
Mänguväli on (peale ülalmainitud koodifixe) täielik, st seal on olemas kõik miinid ja neid ümbritsevatel väljadel on numbrid, mis vastavad omakorda neid välju ümbritsevate miinide arvule. (Tühjad väljad on tähistatud " "-ga.) Oskame ka kursoriga liikuda, kuid mitte "vajutada".

*(Puuduvad osad: mängijale kuvatav mänguväli, sellel väljal oleva informatsiooni järk-järguline kuvamine, kaotus- ja võidutingimused (kuna võidutingimuseks on miinide asukohtade tähistamine ja ülejäänud mängulaua avamine, tuleb võidutingimuse täitmiseks lisada miini tähistamise võimalus). Lõppseisu kuvamine*

Selleks, et mäng oleks "mängitav", ei tohi mängija näha kohe arvutile teadaolevat mänguvälja. Lisame  klassiomaduse, millesse salvestame mängija vaate. Kasutame selleks juba eelnevalt loodud mänguvälja genereerimise funktsiooni self.blank_map("-")

``self.user_view = self.blank_map("-")``

Kasutaja vaate kuvamiseks on vaja muuta funktsioonis self.print_map() üht rida: ``for i, row in enumerate(self.gamemap):`` asemel ``for i, row_list in enumerate(self.user_view):``

Jooksutame kontrolli mõttes koodi.

Nüüd tahame, et selles vaates kriipse andmeteks muuta saaks. Lähme handle_input(self, move) juurde ja lisame enteriga vajutamise tingimuse ning mis peab juhtuma, kui satutakse miini või mõne muu info otsa:

::

    elif move == "":
        cell = self.gamemap[pointer_row][pointer_col]
        # if the cell is not a mine
        if cell != "*":
            self.user_view[pointer_row][pointer_col] = cell
        # else the cell is a mine; return false to indicate losing
        else:
            self.user_view = self.gamemap  # paljastame kogu info
            return False


Võiks koodi jooksutada ja veenduda, et siiani kõik toimib. Veendume, et kasutajakogemust halvendab kõige rohkem see, et mängu ei saa lõpetada. Lähme game(self) kallale, mis praegu näeb välja nii:

::

    def game(self):

        while True:
            self.print_map()
            print()
            move = input()

            self.handle_input(move)


Kuna handle_input(move) abil saame teada, kas mängija komistas miini otsa, saame selles funktsioonis tagastada tõeväärtuse, mille abil otsustame mängu lõpetamise üle.
Salvestame ``self.handle_input(move)`` tulemuse muutujasse: ``handled = self.handle_input(move)``
Lisame tingimused, et erinevate tõeväärtuste olemasolu korral erinevaid tegevusi teha:

::

    if handled:  # hetkel true-d kunagi ei tagastata
        print("You have won!")
        break
    elif handled is None:
        continue
    else:  # avati miin, handled = false
        print("You've lost!")
        break


Katsetame, proovime kaotada. Kuna me ei näe lõplikku mänguvälja, lisada võitu ja kaotusesse ``self.print_map()``
Nüüd vajame võidutingimust. Selleks peame avama kõik ohutud väljad ja märgistama miinid eraldi sümboliga. Sümboliga märgistamine käib näiteks nii **(tükkideks jaotatud osa kohe allpool!)**:
(Peale märgistamise peame suutma ka märgi eemaldada. Samuti tahame teada, mitu märki on - et hiljem kontrollida, kas need vastavad miinide arvule)

::

    elif move == "e":
        cell = self.user_view[pointer_row][pointer_col]
        if cell != "=" and not cell.isdigit() and cell != " ":
            self.user_view[pointer_row][pointer_col] = "="
            self.mark_count += 1
        elif cell == "=":
            self.user_view[pointer_row][pointer_col] = "-"
            self.mark_count -= 1

::

            elif move == "e":
                self.user_view[pointer_row][pointer_col] = "="
        
        # vaja lisada märgistuse tagasivõtmise võimalus
            elif move == "e":
            cell = self.user_view[pointer_row][pointer_col]
            if cell != "=":
                self.user_view[pointer_row][pointer_col] = "="
            elif cell == "=":
                self.user_view[pointer_row][pointer_col] = "-"
        
        # vaja ära keelata info valimatu ülekirjutamine
            elif move == "e":
            cell = self.user_view[pointer_row][pointer_col]
            if cell != "=" and not cell.isdigit() and cell != " ":
                self.user_view[pointer_row][pointer_col] = "="
            elif cell == "=":
                self.user_view[pointer_row][pointer_col] = "-"

Viimaks luua ``self.marker_count`` ja seda märgistamise juures muuta.

Meil on vaja võrrelda, kas kasutaja vaade ja arvuti vaade on võrdväärsed, st kas miinide märgistus langeb kokku miinidega ja muud väljad ühtivad.
Loome uue funktsiooni:

::

    def equal_maps(self):
        view_copy = []

        for row in self.user_view:
            copy_row = []
            for cell in row:
                # https://docs.python.org/3/reference/expressions.html#conditional-expressions
                copy_row.append(cell if cell != "=" else "*")
            view_copy.append(copy_row)

        return view_copy == self.gamemap


Kas kasutaja on kõik miinid märgistanud ja vaated ühtivad? Kontrollime handle_input(move) funktsioonis allpool:

::

    if self.mark_count == self.mine_count and self.equal_maps():
        self.user_view = self.game_map
        # return True to indicate winning
        return True


Ja peakski valmis olema - võib asju *fancy*maks teha:
+ võitmine ilma miine märgistamata?
+ tühjade lahtrite rekursiivne avamine
+ handle_input() meetodis suundade salvestamine sõnastikku (if lausete vähendamine)