# -*- coding: utf-8 -*-

from app import db
from app.models import (News, News_categories, News_imgs,
                         Publications, Publication_categories, Publication_imgs, Publication_type, 
                         Authors, Team)
from datetime import datetime, timedelta


def News_db():
        news = News.query.all()
        for u in news:
                db.session.delete(u)
        news_c = News_categories.query.all()
        for u in news_c:
                db.session.delete(u)
        db.session.commit()

        c1 = News_categories(category='Geocronologia')
        c2 = News_categories(category='Hidrogeologia')
        c3 = News_categories(category='Economica') 

        db.session.add_all([c1, c2, c3])
        db.session.commit()

        imgs_p1 = News_imgs(img_path='/static/news/imgs/new_1-1.jpg')
        imgs_p2 = News_imgs(img_path='/static/imgs/Pub_1_.jpg')
        imgs_p3 = News_imgs(img_path='/static/imgs/news_1.jpg')
        imgs_p4 = News_imgs(img_path='/static/imgs/Pub_3.jpg')
        imgs_p5 = News_imgs(img_path='https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20(34).jpg')
        imgs_p6 = News_imgs(img_path='/static/imgs/Pub_2.png')
        imgs_p7 = News_imgs(img_path='https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20(34).jpg')
        imgs_p8 = News_imgs(img_path='https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20(34).jpg')
        imgs_p9 = News_imgs(img_path='/static/imgs/Pub_3.jpg')
        imgs_p10 = News_imgs(img_path='https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20(34).jpg')
        imgs_p11 = News_imgs(img_path='/static/imgs/Pub_2.png')
        imgs_p12 = News_imgs(img_path='https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20(34).jpg')

        db.session.add_all([imgs_p1, imgs_p2, imgs_p3, imgs_p4])
        db.session.commit()


        body = '''Breve introducao da noticia. Donec sed odio dui. Etiam porta 
                sem malesuada magna mollis euismod. Nullam id dolor id nibh ultricies vehicula ut id elit. 
                Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Praesent commodo cursus magna.
                '''

        intro = '''Breve introducao da noticia. Donec sed odio dui. Etiam porta 
                sem malesuada magna mollis euismod. Nullam id dolor id nibh ultricies vehicula ut id elit. 
                Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Praesent commodo cursus magna.
                '''
        title= 'Titulo da Noticia'


        title1= 'CPRM, ANP e Petrobras assinam Plano de Ação que norteará um amplo programa de trabalho conjunto'
        intro1 = " No dia 23 de fevereiro, o Serviço Geológico do Brasil, a Agência Nacional do Petróleo e a Petrobras assinaram um Plano de Ação com o objetivo de promover um amplo programa de pesquisa e inovação na área de geociências com foco principal em óleo e gás."

        body1 = '''No dia 23 de fevereiro, o Serviço Geológico do Brasil, a Agência Nacional do Petróleo e a Petrobras assinaram um Plano de Ação com o objetivo de promover um amplo programa de pesquisa e inovação na área de geociências com foco principal em óleo e gás. Este plano marca o início de atividades conjuntas entre as três instituições que permitirão através de projetos de P&D promover ampla reforma do Museu de Ciências da Terra, a ampliação da Rede de Litotecas e a construção dos laboratórios de microanálise química e isotópica (Laboratório de Preparação de Amostras, Laboratório de Imageamento e Análise Mineral, Laboratório de Petrocronologia e Traçadores Isotópicos, Laboratório de Termocronologia e Gases Nobres e Laboratório de Isótopos Estáveis Avançado (NanoSIMS)) que comporão o Centro de Referência em Geociências. A ampliação da Rede de Litotecas do SGB/CPRM permitirá o armazenamento e administração de todo o acervo de amostras de rocha e gás do país com destaque para o material obtido nos mais de 60 anos de existência da Petrobras. Na ocasião foi apresentado o cronograma dessas ações com início das atividades em 2018 e conclusão em 2025.
        O documento foi assinado pelo Chefe do Centro de Desenvolvimento Tecnológico do SGB/CPRM, Noevaldo Araújo Teixeira, pelo Superintendente de Dados Técnicos da ANP, Cláudio Jorge Martins de Souza, pelo Gerente-Geral de Geologia e Petrofísica da Petrobras, Otaviano da Cruz Pessoa Neto e pelo Gerente-Geral de P&D em Exploração e Produção do Centro de Pesquisa da Petrobras, Farid Salomão Shecaira. O momento contou com a presença do Diretor de Administração e Finanças do SGB/CPRM, Juliano Oliveira, que tem sido um entusiasta pela parceria.
        Todas essas iniciativas estarão suportadas por um robusto portfólio de projetos de P&D tendo o Serviço Geológico como líder e operador principal.  As linhas de pesquisa já acordadas com a ANP versarão sobre estratigrafia, geodinâmica do Atlântico Sul e Equatorial, geodiversidade e impactos ambientais, arquitetura listosférica e sistemas minerais e recursos renováveis e minerais para o futuro. Tais linhas podem ser ampliadas e modificadas dependendo de acordo entre as áreas interessadas.
        Na reunião, tanto a Petrobras, quanto a ANP, ressaltaram que a ampliação das instalações da Rede de Litotecas do SGB/CPRM constitui uma enorme responsabilidade e propiciará certamente uma nova onda de projetos científicos não só pelo SGB/CPRM, mas de toda comunidade acadêmica nacional. A criação do Centro de Referência em Geociências (Laboratórios) constitui um antigo anseio do corpo técnico do SGB/CPRM e trará como consequência imediata uma melhor qualificação científica em todos os projetos da instituição. A reforma, ampliação e modernização do Museu de Ciências da Terra pode ser definido como o resgate de parte da memória geológica do nosso país.
        Todos os presentes ressaltaram que a assinatura do plano de trabalho firmado entre a Petrobras, ANP e SGB/CPRM colocará o Serviço Geológico em uma nova dimensão tendo como parceiros a principal empresa brasileira de óleo e gás e uma das mais importantes agências reguladoras do país. Tudo isso visará à produção de projetos de P&D compromissados com o setor produtivo de óleo e gás e o setor mineral brasileiro. O chefe do CEDES, Noevaldo Teixeira, afirma que “o objetivo da atual presidência é tornar o SGB/CPRM uma referência entre os principais serviços geológicos mundiais”. Noevaldo ressalta ainda que “o documento assinado resulta de um esforço coletivo, tendo a frente a coordenação do chefe do Departamento de Relações Institucionais e Divulgação, Marco Tulio Naves de Carvalho”. 
        '''

        file1 = '/static/news/files/new_1-1.pdf'

        now = datetime.utcnow()
        n1 = News(title=title, category=c1, body=body, intro=intro,
                date=now + timedelta(seconds=1))
        n2 = News(title=title, category=c2, body=body, intro=intro,
                date=now + timedelta(seconds=100))
        n3 = News(title=title, category=c3, body=body, intro=intro,
                date=now + timedelta(seconds=500))
        n4 = News(title=title, category=c2, body=body, intro=intro,
                date=now + timedelta(seconds=1000))
        n5 = News(title=title, category=c1, body=body, intro=intro,
                date=now + timedelta(seconds=1200))
        n6 = News(title=title, category=c2, body=body, intro=intro,
                date=now + timedelta(seconds=1500))
        n7 = News(title=title, category=c3, body=body, intro=intro,
                date=now + timedelta(seconds=2000))
        n8 = News(title=title, category=c2, body=body, intro=intro,
                date=now + timedelta(seconds=2200))
        n9 = News(title=title, category=c1, body=body, intro=intro,
                date=now + timedelta(seconds=2500))
        n10 = News(title=title, category=c2, body=body, intro=intro,
                date=now + timedelta(seconds=3000))
        n11 = News(title=title, category=c3, body=body, intro=intro,
                date=now + timedelta(seconds=3200))
        n12 = News(title=title1, category=c2, body=body1, intro=intro1,
                date=now + timedelta(seconds=3500), file_dir=file1)

        n1.imgs_dir.append(imgs_p12)
        n2.imgs_dir.append(imgs_p2)
        n3.imgs_dir.append(imgs_p3)
        n4.imgs_dir.append(imgs_p4)
        n5.imgs_dir.append(imgs_p5)
        n6.imgs_dir.append(imgs_p6)
        n7.imgs_dir.append(imgs_p7)
        n8.imgs_dir.append(imgs_p8)
        n9.imgs_dir.append(imgs_p9)
        n10.imgs_dir.append(imgs_p10)
        n11.imgs_dir.append(imgs_p11)
        n12.imgs_dir.append(imgs_p1)


        db.session.add_all([n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12])
        db.session.commit()

def Pub_db():
        pubs = Publications.query.all()
        for u in pubs:
                db.session.delete(u)
        pubs_c = Publication_categories.query.all()
        for u in pubs_c:
                db.session.delete(u)
        pubs_c = Publication_imgs.query.all()
        for u in pubs_c:
                db.session.delete(u)
        pubs_c = Publication_type.query.all()
        for u in pubs_c:
                db.session.delete(u)
        auth = Authors.query.all()
        for u in auth:
                db.session.delete(u)
        db.session.commit()

        c1 = Publication_categories(category='Economica')
        c2 = Publication_categories(category='Modelamento')
        c3 = Publication_categories(category='Tectonica') 
        c4 = Publication_categories(category='Laboratório') 

        db.session.add_all([c1, c2, c3, c4])
        db.session.commit()

        auth1 = Authors(name='Andrew Peter James', abrev='James A.J.')
        auth2 = Authors(name='Bob Dilan', abrev='Dilan B.')
        auth3 = Authors(name='Oliver Twist', abrev='Oliver T.')
        auth4 = Authors(name='Christian Michel Lacasse', abrev='Lacasse C.M.')

        db.session.add_all([auth1, auth2, auth3, auth4])
        db.session.commit()

        pub_type1 = Publication_type(pub_type='Artigo em Jornal')
        pub_type2 = Publication_type(pub_type='Artigo em Revista')
        pub_type3 = Publication_type(pub_type='Livro')
        pub_type4 = Publication_type(pub_type='Tese')
        pub_type5 = Publication_type(pub_type='Nota Técnica')

        db.session.add_all([pub_type1, pub_type2, pub_type3, pub_type4, pub_type5])
        db.session.commit()

        imgs_p1 = Publication_imgs(img_path='/static/pubs/imgs/pub_1-1.jpg', img_subtitle='Exemplo de mapeamento composicional e textura interna de minerais utilizando Microscópio Eletrônico de Varredura (MEV).')
        imgs_p2 = Publication_imgs(img_path='/static/imgs/Pub_2.png')
        imgs_p3 = Publication_imgs(img_path='/static/imgs/Pub_3.jpg')
        imgs_p4 = Publication_imgs(img_path='/static/imgs/Pub_1_.jpg')
        

        db.session.add_all([imgs_p1, imgs_p2, imgs_p3, imgs_p4])
        db.session.commit()

        intro = '''
                Hyperspectral image classification is an important task in remote sensing image analysis. Traditional machine learning techniques are difficult to deal with hyperspectral images directly, because hyperspectral images have too many redundant spectral channels. In this paper we propose a novel method for hyperspectral image classification, by which spectral and spatial features are jointly exploited from hyperspectral images. Firstly, considering the local similarity in spatial domain, we employ a large spatial window to get image blocks from hyperspectral image Secondly, each spectral channel of the image block is filtered to extract their spatial and spectral features, after that the features are merged by convolutional layers. Finally, the fully-connected layers are used to get the classification result. Comparing with other state-of-the-art techniques, the proposed method pays more attention to the correlation of spatial neighborhood by using a large spatial window in the network. In addition, we combine the proposed network with the traditional support vector machine (SVM) classifier to improve the performance of hyperspectral image classification. Moreover, an adaptive method of the spatial window sizes selection is proposed in this paper. Experimental results conducted on the AVIRIS and ROSIS datasets demonstrate that the proposed method outperforms the state-of-the-art techniques.
                '''

        title = 'Titulo Publicação1 Titulo Publicação Titulo Publicação Titulo Publicação Titulo Publicação'

        title1 = 'Projeto Conceitual do Centro de Referência em Geociências (Laboratórios)'

        intro1 = '''
                Esta nota técnica apresenta os laboratórios técnicos que deverão constituir o Centro de Referencia em Geociências, para microanálise química e isotópica a ser construído no Serviço Geológico do Brasil, na cidade do Rio de Janeiro. Os laboratórios estão separados em cinco diferentes frentes que incluem: a) Laboratório de Preparação de Amostras; b) Laboratório de MIcroimageamento e Análise Mineral; c) Laboratório de Petrocronologia e Traçadores Isotópicos; d) Laboratório de Termocronologia Avançada e Gases Nobres; e) Laboratório de Isótopos Estáveis Avançado (NanoSIMS). O total a ser investido em equipamentos é de 15,5 M US$ e o cronograma de implementação e construção é de 18 meses. Os laboratórios deverão operar de maneira colaborativa, comercial e por meio de projetos de P&D. A reunião de diversos laboratórios com vocações distintas em um único centro deve acelerar o conhecimento geológico do país, sobretudo na área das bacias sedimentares, trazendo retorno para o setor produtivo de Óleo & Gás e Mineração.
                '''
        

        file1 = '/static/pubs/pdf/pub_1-1.pdf'

        now = datetime.utcnow()
        p1 = Publications(title=title, category=c1, file_dir='/static/pdf/pub_ex.pdf', abstract=intro,
                date=now + timedelta(seconds=1), pub_type=pub_type1)
        p2 = Publications(title=title, category=c2, file_dir='/static/pdf/pub_ex.pdf', abstract=intro,
                date=now + timedelta(seconds=1000), pub_type=pub_type2)
        
        p3 = Publications(title=title, category=c3, file_dir='/static/pdf/pub_ex.pdf', abstract=intro,
                date=now + timedelta(seconds=10000), pub_type=pub_type3)

        p4 = Publications(title=title1, category=c4, file_dir=file1, abstract=intro1,
                date=now + timedelta(seconds=20000), pub_type=pub_type5)

        p1.authors.append(auth1)
        p1.authors.append(auth2)
        p1.authors.append(auth3)
        p1.authors.append(auth4)
        p2.authors.append(auth2)
        p2.authors.append(auth3)
        p2.authors.append(auth4)
        p3.authors.append(auth1)
        p3.authors.append(auth2)
        p4.authors.append(auth4)

        p1.imgs_dir.append(imgs_p4)
        p2.imgs_dir.append(imgs_p2)
        p3.imgs_dir.append(imgs_p3)
        p4.imgs_dir.append(imgs_p1)]

        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

     
def Team_db():
        team = Team.query.all()
        for u in team:
                db.session.delete(u)
        db.session.commit()
        intro = '''
                Dmosnin ed osan pojd kaxsax ckdds a dolkcm sd cnoia. Dmosnin ed osan pojd kaxsax ckdds a dolkcm sd cnoia.
                Dmosnin ed osan pojd kaxsax ckdds a dolkcm sd cnoia. 
                '''

        now = datetime.utcnow()
        name1="Martin L. King"
        name2="Bob Dylan"
        name3="James Brown"
        name4="Dee Purple"
        name5="John Lenon"
        name6="Steve Jobs"

        role1="Diretor"
        role2="Pesquisador"
        role3="Pesquisador Chefe"

        t1 = Team(name=name1, role=role1, intro=intro, foto="/static/imgs/face.jpg")
        t2 = Team(name=name2, role=role3, intro=intro, foto="/static/imgs/face.jpg")
        t3 = Team(name=name3, role=role2, intro=intro, foto="/static/imgs/face.jpg")
        t4 = Team(name=name4, role=role2, intro=intro, foto="/static/imgs/face.jpg")
        t5 = Team(name=name5, role=role2, intro=intro, foto="/static/imgs/face.jpg")
        t6 = Team(name=name6, role=role2, intro=intro, foto="/static/imgs/face.jpg")


        db.session.add_all([t1, t2, t3, t4, t5, t6])
        db.session.commit()
News_db()
Pub_db()
Team_db()
