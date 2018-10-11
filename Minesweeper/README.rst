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

**TODO: koolituse esimese osa samm-sammuline kirjeldus**

Loodi minesweeperi klass. Klassiomaduste hulgas on mänguvälja mõõtmed, miinide arv, kursori asukoht ja arvutile teadaolev mänguvali (ehk lõpus avalduv mänguväli).
Mänguväli on (peale ülalmainitud koodifixe) täielik, st seal on olemas kõik miinid ja neid ümbritsevatel väljadel on numbrid, mis vastavad omakorda neid välju ümbritsevate miinide arvule.


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
Nüüd vajame võidutingimust. Selleks peame avama kõik ohutud väljad ja märgistama miinid eraldi sümboliga. Sümboliga märgistamine käib näiteks nii:
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


Meil on vaja võrrelda, kas kasutaja vaade ja arvuti vaade on võrdväärsed, st kas miinide märgistus langeb kokku miinidega ja muud väljad ühtivad.
Loome uue funktsiooni:

::

    def equal_maps(self):
        view_copy = []

        for row in self.user_view:
            copy_row = []
            for cell in row:
                copy_row.append(cell if cell != "=" else "*")
            view_copy.append(copy_row)

        return view_copy == self.gamemap


Kas kasutaja on kõik miinid märgistanud ja vaated ühtivad? Kontrollime handle_input(move) funktsioonis allpool:

::

    if self.mark_count == self.mine_count and self.equal_maps():
        self.user_view = self.game_map
        # return True to indicate winning
        return True


Ja peakski valmis olema - võib asju fancymaks teha