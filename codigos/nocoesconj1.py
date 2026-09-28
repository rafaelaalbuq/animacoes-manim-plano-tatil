from manim import*

class conjuntos(Scene):
    def construct(self):

       
        self.camera.background_color =  WHITE   

        try:
            img = ImageMobject('logounivasfbranca').scale(0.2)
            img.to_corner(DR, buff = 0.1)
            self.add(img)
        except:
            print('LOGO NAO ENCONTRADA')    


    #relações ELEMENTO X CONJUNTO

        conj1_label = Tex(r'A = \{a, b, c\}').set_color(PURE_RED).scale(1.2).to_edge(UP+LEFT, buff = 0.2)#imprmir as chaves no video
        conj2_label = Tex(r'B = \{c, d, e\}').set_color(PURE_GREEN).scale(1.2).next_to(conj1_label, DOWN, buff=0.5)
        
        conjA_label = Tex(r'A').set_color(PURE_RED).scale(1.2)
        conjB_label = Tex(r'B').set_color(PURE_GREEN).scale(1.2)

        conj1_elipse = Ellipse(width=3, height=6, color=PURE_RED).shift(LEFT*1)
        conj2_elipse = Ellipse(width=3, height=6, color=PURE_GREEN).shift(RIGHT*3)

        elem1 = Tex(r'a').set_color(BLACK).scale(2.5)
        elem2 = Tex(r'b').set_color(BLACK).scale(2.5)
        elem3 = Tex(r'c').set_color(BLACK).scale(2.5)
        elem4 = Tex(r'c').set_color(BLACK).scale(2.5)
        elem5 = Tex(r'd').set_color(BLACK).scale(2.5)
        elem6 = Tex(r'e').set_color(BLACK).scale(2.5)

        grupo1 = VGroup(elem1, elem2, elem3).arrange(DOWN, buff=0.8).move_to(conj1_elipse.get_center())
        grupo2 = VGroup(elem4, elem5, elem6).arrange(DOWN, buff=0.8).move_to(conj2_elipse.get_center())

        # posicionar rótulo e grupo relativamente à elipse antes de agrupar
        conjA_label.next_to(conj1_elipse, UP)
        grupo1.move_to(conj1_elipse.get_center())

        # agrupar a elipse, o rótulo e os elementos para mover tudo junto
        conj1_group = VGroup(conj1_elipse, conjA_label, grupo1)

        conjB_label.next_to(conj2_elipse, UP)
        grupo2.move_to(conj2_elipse.get_center())

        conj2_group = VGroup(conj2_elipse, conjB_label, grupo2)
     
        rel1 = Tex(r'$a \in A$').set_color(BLACK).scale(2)
        rel2 = Tex(r'$b \in A$').set_color(BLACK).scale(2).next_to(rel1, DOWN, buff=0.5)
        rel3 = Tex(r'$c \in A$').set_color(BLACK).scale(2).next_to(rel2, DOWN, buff=0.5)
        rel4 = Tex(r'$c \in B$').set_color(BLACK).scale(2)
        rel5 = Tex(r'$d \in B$').set_color(BLACK).scale(2).next_to(rel4, DOWN, buff=0.5)
        rel6 = Tex(r'$e \in B$').set_color(BLACK).scale(2).next_to(rel5, DOWN, buff=0.5)
        rel7 = Tex(r'$a \notin B$').set_color(BLACK).scale(2).next_to(rel6, DOWN, buff=0.5)
        rel8 = Tex(r'$e \notin A$').set_color(BLACK).scale(2).next_to(rel3, DOWN, buff=0.5)    

        relA = VGroup(rel1, rel2, rel3, rel8).move_to(ORIGIN)
        relB = VGroup(rel4, rel5, rel6, rel7).move_to(ORIGIN)

        subconja1 = Tex(r'A = \{ \{a\}, \{b\}, \{c\} \}').set_color(PURE_RED).scale(1.5).to_edge(UP, buff=0.5)
        
        subconja2 = Tex(r'$\{a\} \subset A$').set_color(BLACK).scale(1.5)
        subconja3 = Tex(r'$\{b\} \subset A$').set_color(BLACK).scale(1.5).next_to(subconja2, DOWN, buff=0.3)
        subconja4 = Tex(r'$\{c\} \subset A$').set_color(BLACK).scale(1.5).next_to(subconja3, DOWN, buff=0.3)
        subconja5 = Tex(r'$\{  \} \subset A$').set_color(BLACK).scale(1.5).next_to(subconja4, DOWN, buff=0.3)
        subconja6 = Tex(r'$\{e\} \not\subset A$').set_color(BLACK).scale(1.5).next_to(subconja5, DOWN, buff=0.3)

        subconjA = VGroup(subconja2, subconja3, subconja4, subconja5, subconja6).next_to(subconja1, DOWN, buff=0.8)
   
   
        subconjB1 = Tex(r'B = \{ \{c\}, \{d\}, \{e\} \}').set_color(PURE_GREEN).scale(1.5).to_edge(UP, buff=0.5)
        
        subconjb2 = Tex(r'$\{c\} \subset B$').set_color(BLACK).scale(1.5)
        subconjb3 = Tex(r'$\{d\} \subset B$').set_color(BLACK).scale(1.5).next_to(subconjb2, DOWN, buff=0.3)
        subconjb4 = Tex(r'$\{e\} \subset B$').set_color(BLACK).scale(1.5).next_to(subconjb3, DOWN, buff=0.3)
        subconjb5 = Tex(r'$\{  \} \subset B$').set_color(BLACK).scale(1.5).next_to(subconjb4, DOWN, buff=0.3)
        subconjb6 = Tex(r'$\{a\} \not\subset B$').set_color(BLACK).scale(1.5).next_to(subconjb5, DOWN, buff=0.3)

        subconjB = VGroup(subconjb2, subconjb3, subconjb4, subconjb5, subconjb6).next_to(subconjB1, DOWN, buff=0.8)
   
   
   
    #relaçoes CONJ X CONJ    




        self.play(Write(conj1_label))
        self.play(Write(conj2_label))
        self.wait(1)
        self.play(Create(conj1_elipse), Create(conj2_elipse))
        
        # os positions já foram definidos acima; apenas escrevemos os rótulos
        self.play(Write(conjA_label), Write(conjB_label))
        self.play(FadeIn(grupo1), FadeIn(grupo2))

        self.play(FadeOut(conj1_label), FadeOut(conj2_label))
        self.play(FadeOut(conj2_group))

        # mover conjunto (elipse + rótulo + elementos) para o canto superior esquerdo
        self.play(conj1_group.animate.to_edge(UP+LEFT, buff=0.5))
        self.wait(2)
        #colocar as relaçoes de pertence aqui
        self.play(Write(relA))
        self.wait(3)
        self.play(FadeOut(relA))
        self.wait()
        self.play(FadeOut(conj1_group))
        self.wait()
        self.play(Write(subconja1))
        self.wait()
        self.play(Write(subconjA))
        self.wait(2)
        self.play(FadeOut(subconja1), FadeOut(subconjA))
        self.wait()
        
        # posicionar `conj2_group` onde `conj1_group` ficou e trocar
        conj2_group.move_to(conj1_group.get_center())

        self.play(FadeIn(conj2_group))
        self.wait(2)
        self.play(Write(relB))
        self.wait(3)
        self.play(FadeOut(relB))
        self.wait()
        self.play(FadeOut(conj2_group))
        self.wait()
        self.play(Write(subconjB1))
        self.wait()
        self.play(Write(subconjB))
        self.wait(2)
        self.play(FadeOut(subconjB1), FadeOut(subconjB))
        self.wait(2)

        #caso n adc novas relaçoes, centralizar itens


        #RELAÇOES CONJ X CONJ




        
    
        



    


