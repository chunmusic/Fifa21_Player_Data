import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from PIL import Image


def init_ui():

    st.set_page_config(page_title="FIFA Player",
                    page_icon="🧊",
                    layout="wide",
                    initial_sidebar_state="expanded")

   
    st.markdown("<h1 style='text-align: center; color: black;font-size:72px'>FIFA 21 - Player Database</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: black;font-size:72px'></h1>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.beta_columns(4)

    placeholder_1 = col2.empty()
    placeholder_2 = col3.empty()

    sub_col1,sub_col2,sub_col3,sub_col4,sub_col5,sub_col6 = st.beta_columns((2,1,1,1,1,2))


    return col1,col2,col3,col4,sub_col1,sub_col2,sub_col3,sub_col4,sub_col5,sub_col6,placeholder_1,placeholder_2

def select_player_1(col1,col2,sub_col2,sub_col3):
    
    league_name = col1.selectbox("LEAGUE",("PREMIER LEAGUE - ENGLAND","LA LIGA - SPAIN","BUNDESLIGA - GERMANY", \
                                        "SERIE A - ITALY","LIGUE 1 - FRANCE"),1,key="league_1") # Use index 1 for Laliga Spain

    if (league_name == "PREMIER LEAGUE - ENGLAND"):
        club_name_1 = col1.selectbox("CLUB",("Arsenal","Aston Villa","Brighton & Hove Albion","Burnley","Chelsea","Crystal Palace","Everton","Fulham", \
                                        "Leeds United","Leicester City","Liverpool","Manchester City","Manchester United","Newcastle United", \
                                        "Sheffield United","Southampton","Tottenham Hotspur","West Bromwich Albion","West Ham United","Wolverhampton Wanderers"),key="england_1")
    elif (league_name == "LA LIGA - SPAIN"):
        club_name_1 = col1.selectbox("CLUB",("Athletic Club","Atlético de Madrid","CA Osasuna","Cádiz CF","D. Alavés","Elche CF","FC Barcelona", \
                                                 "Getafe CF","Granada CF","Levante UD","R. Valladolid CF","RC Celta","Real Betis Balompié","Real Madrid", \
                                                 "Real Sociedad","SD Eibar","SD Huesca","Sevilla FC","Valencia CF","Villarreal CF"),6,key="spain_1") # Use index 6 for Barcelona
    elif (league_name == "BUNDESLIGA - GERMANY"):
        club_name_1 = col1.selectbox("CLUB",("1. FC Köln","1. FSV Mainz 05","DSC Arminia Bielefeld","Borussia Dortmund","FC Augsburg","FC Bayern München", \
                                                 "FC Schalke 04","Eintracht Frankfurt","Hertha Berlin","Bayer 04 Leverkusen","Borussia Mönchengladbach", \
                                                 "RB Leipzig","Sport-Club Freiburg","TSG Hoffenheim","1. FC Union Berlin","VfB Stuttgart","VfL Wolfsburg", \
                                                 "SV Werder Bremen"),key="germany_1")
    elif (league_name == "SERIE A - ITALY"):
        club_name_1 = col1.selectbox("CLUB",("Atalanta","Benevento","Bologna","Cagliari","Crotone","Fiorentina","Genoa","Hellas Verona","Inter", \
                                                 "La Spezia","Lazio","Milan","Napoli","Parma","Juventus","Roma","Sampdoria","Sassuolo","Torino","Udinese"),key="italy_1")
    elif (league_name == "LIGUE 1 - FRANCE"):
        club_name_1 = col1.selectbox("CLUB",("Angers SCO","AS Monaco","AS Saint-Étienne","FC Girondins de Bordeaux","Dijon FCO","FC Lorient","FC Metz", \
                                                 "FC Nantes","LOSC Lille","Montpellier Hérault SC","Nîmes Olympique","OGC Nice","Olympique Lyonnais", \
                                                 "Olympique de Marseille","Paris Saint-Germain","RC Lens","Stade Rennais FC","Stade Brestois 29","Stade de Reims", \
                                                 "RC Strasbourg Alsace"),key="france_1")

    df = pd.read_csv("dataset/2021.csv")
    df = df.loc[df['Club'] == club_name_1].sort_values(by='Overal', ascending=False)
    player_1_df = df['Name']

    player_1_name = col1.selectbox("PLAYER",(list(player_1_df)),key="player_1")
    
    player_1_id = df.loc[df['Name'] == player_1_name,'ID'].iloc[0]

    image = "https://media.contentapi.ea.com/content/dam/ea/fifa/fifa-21/ratings-collective/f20assets/player-headshots/" + str(player_1_id) + ".png"

    sub_col1.image(image, use_column_width=True)

    sub_col1.markdown(f"<h1 style='text-align: center; color: black;font-size:30px'>{player_1_name}</h1>", unsafe_allow_html=True)

    preferred_position_1 = df.loc[df['Name'] == player_1_name,'PreferredPositions'].iloc[0]
    sub_col1.markdown(f"<h2 style='text-align: center; color: black;font-size:24px'>{preferred_position_1}</h2>", unsafe_allow_html=True)


    #Nationality
    player_1_nationality = df.loc[df['Name'] == player_1_name,'Natinality'].iloc[0]
    sub_col2.markdown(f"<h4 style='text-align: left; color: black;font-size:18px'>Nationality:</h4>", unsafe_allow_html=True)
    sub_col3.markdown(f"<h4 style='text-align: left; color: black;font-size:18px'>{player_1_nationality}</h4>", unsafe_allow_html=True)

    #Age
    player_1_age = df.loc[df['Name'] == player_1_name,'Age'].iloc[0]
    sub_col2.markdown(f"<h4 style='text-align: left; color: black;font-size:18px'>Age: </h4>", unsafe_allow_html=True)
    sub_col3.markdown(f"<h4 style='text-align: left; color: black;font-size:18px'>{player_1_age}</h4>", unsafe_allow_html=True)

    #Height
    player_1_height = df.loc[df['Name'] == player_1_name,'Height'].iloc[0]
    sub_col2.markdown(f"<h4 style='text-align: left; color: black;font-size:18px'>Height: </h4>", unsafe_allow_html=True)
    sub_col3.markdown(f"<h4 style='text-align: left; color: black;font-size:18px'>{player_1_height}</h4>", unsafe_allow_html=True)

    #Preferred Foot
    player_1_pff = df.loc[df['Name'] == player_1_name,'PreferredFoot'].iloc[0]
    sub_col2.markdown(f"<h4 style='text-align: left; color: black;font-size:18px'>Preferred Foot: </h4>", unsafe_allow_html=True)
    sub_col3.markdown(f"<h4 style='text-align: left; color: black;font-size:18px'>{player_1_pff}</h4>", unsafe_allow_html=True)


    for i in range(24,58):  #index 24 is ballcontrol and index 57 is gkreflexes
        col_name = df.columns[i]
        col_data = df.loc[df['Name'] == player_1_name, df.columns[i]].iloc[0]
        sub_col2.markdown(f"<h4 style='text-align: left; color: black;font-size:18px'>{col_name}: </h4>", unsafe_allow_html=True)

        if col_data >=95 and col_data<=99:
            sub_col3.markdown(f"<h4 style='text-align: left; color: #C0392B;font-size:18px'>{col_data}</h4>", unsafe_allow_html=True)
        elif col_data >=90 and col_data<=94:
            sub_col3.markdown(f"<h4 style='text-align: left; color: #E67E22;font-size:18px'>{col_data}</h4>", unsafe_allow_html=True)
        elif col_data >=80 and col_data<=89:
            sub_col3.markdown(f"<h4 style='text-align: left; color: #F1C40F;font-size:18px'>{col_data}</h4>", unsafe_allow_html=True)
        elif col_data >=75 and col_data<=79:
            sub_col3.markdown(f"<h4 style='text-align: left; color: #BFF517;font-size:18px'>{col_data}</h4>", unsafe_allow_html=True)
        elif col_data >=0 and col_data<=74:
            sub_col3.markdown(f"<h4 style='text-align: left; color: grey;font-size:18px'>{col_data}</h4>", unsafe_allow_html=True)


    player_1_att = (df.loc[df['Name'] == player_1_name,'AttPosition'].iloc[0]+df.loc[df['Name'] == player_1_name,'Finishing'].iloc[0])/2
    player_1_spd = (df.loc[df['Name'] == player_1_name,'SprintSpeed'].iloc[0]+df.loc[df['Name'] == player_1_name,'Acceleration'].iloc[0])/2
    player_1_pow = df.loc[df['Name'] == player_1_name,'ShotPower'].iloc[0]
    player_1_sta = df.loc[df['Name'] == player_1_name,'Stamina'].iloc[0]
    player_1_tec = (df.loc[df['Name'] == player_1_name,'BallControl'].iloc[0]+df.loc[df['Name'] == player_1_name,'Dribbling'].iloc[0])/2

    if preferred_position_1 == "GK":
        player_1_def = (df.loc[df['Name'] == player_1_name,'GKPositioning'].iloc[0]+df.loc[df['Name'] == player_1_name,'GKDiving'].iloc[0]+df.loc[df['Name'] == player_1_name,'GKHandling'].iloc[0]+df.loc[df['Name'] == player_1_name,'GKKicking'].iloc[0]+df.loc[df['Name'] == player_1_name,'GKReflexes'].iloc[0])/5
    else:
        player_1_def = (df.loc[df['Name'] == player_1_name,'Marking'].iloc[0]+df.loc[df['Name'] == player_1_name,'SlideTackle'].iloc[0]+df.loc[df['Name'] == player_1_name,'StandTackle'].iloc[0])/3


    return player_1_att,player_1_spd,player_1_pow,player_1_def,player_1_sta,player_1_tec

def select_player_2(col4,col3,sub_col4,sub_col5):

    league_name2 = col4.selectbox("LEAGUE",("PREMIER LEAGUE - ENGLAND","LA LIGA - SPAIN","BUNDESLIGA - GERMANY", \
                                        "SERIE A - ITALY","LIGUE 1 - FRANCE"),3,key="league_2") #Use index 3 for Serie A Italy


    if (league_name2 == "PREMIER LEAGUE - ENGLAND"):
        club_name_2 = col4.selectbox("CLUB",("Arsenal","Aston Villa","Brighton & Hove Albion","Burnley","Chelsea","Crystal Palace","Everton","Fulham", \
                                        "Leeds United","Leicester City","Liverpool","Manchester City","Manchester United","Newcastle United", \
                                        "Sheffield United","Southampton","Tottenham Hotspur","West Bromwich Albion","West Ham United","Wolverhampton Wanderers"),key="england_2")
    elif (league_name2 == "LA LIGA - SPAIN"):
        club_name_2 = col4.selectbox("CLUB",("Athletic Club","Atlético de Madrid","CA Osasuna","Cádiz CF","D. Alavés","Elche CF","FC Barcelona", \
                                                 "Getafe CF","Granada CF","Levante UD","R. Valladolid CF","RC Celta","Real Betis Balompié","Real Madrid", \
                                                 "Real Sociedad","SD Eibar","SD Huesca","Sevilla FC","Valencia CF","Villarreal CF"),key="spain_2")
    elif (league_name2 == "BUNDESLIGA - GERMANY"):
        club_name_2 = col4.selectbox("CLUB",("1. FC Köln","1. FSV Mainz 05","DSC Arminia Bielefeld","Borussia Dortmund","FC Augsburg","FC Bayern München", \
                                                 "FC Schalke 04","Eintracht Frankfurt","Hertha Berlin","Bayer 04 Leverkusen","Borussia Mönchengladbach", \
                                                 "RB Leipzig","Sport-Club Freiburg","TSG Hoffenheim","1. FC Union Berlin","VfB Stuttgart","VfL Wolfsburg", \
                                                 "SV Werder Bremen"),key="germany_2")
    elif (league_name2 == "SERIE A - ITALY"):
        club_name_2 = col4.selectbox("CLUB",("Atalanta","Benevento","Bologna","Cagliari","Crotone","Fiorentina","Genoa","Hellas Verona","Inter", \
                                                 "Juventus","La Spezia","Lazio","Milan","Napoli","Parma","Roma","Sampdoria","Sassuolo","Torino","Udinese"),9,key="italy_2") #Use index 10 for Juventus
    elif (league_name2 == "LIGUE 1 - FRANCE"):
        club_name_2 = col4.selectbox("CLUB",("Angers SCO","AS Monaco","AS Saint-Étienne","FC Girondins de Bordeaux","Dijon FCO","FC Lorient","FC Metz", \
                                                 "FC Nantes","LOSC Lille","Montpellier Hérault SC","Nîmes Olympique","OGC Nice","Olympique Lyonnais", \
                                                 "Olympique de Marseille","Paris Saint-Germain","RC Lens","Stade Rennais FC","Stade Brestois 29","Stade de Reims", \
                                                 "RC Strasbourg Alsace"),key="france_2")

    df = pd.read_csv("dataset/2021.csv")
    df = df.loc[df['Club'] == club_name_2].sort_values(by='Overal', ascending=False)
    player_2_df = df['Name']

    player_2_name = col4.selectbox("PLAYER",(list(player_2_df)),key="player_2")
    player_2_id = df.loc[df['Name'] == player_2_name,'ID'].iloc[0]

    image2 = "https://media.contentapi.ea.com/content/dam/ea/fifa/fifa-21/ratings-collective/f20assets/player-headshots/" + str(player_2_id) + ".png"

    sub_col6.image(image2, use_column_width=True)

    sub_col6.markdown(f"<h1 style='text-align: center; color: black;font-size:30px'>{player_2_name}</h1>", unsafe_allow_html=True)

    preferred_position_2 = df.loc[df['Name'] == player_2_name,'PreferredPositions'].iloc[0]
    sub_col6.markdown(f"<h2 style='text-align: center; color: black;font-size:24px'>{preferred_position_2}</h2>", unsafe_allow_html=True)


    #Nationality
    player_2_nationality = df.loc[df['Name'] == player_2_name,'Natinality'].iloc[0]
    sub_col4.markdown(f"<h4 style='text-align: left; color: black;font-size:18px'>Nationality:</h4>", unsafe_allow_html=True)
    sub_col5.markdown(f"<h4 style='text-align: left; color: black;font-size:18px'>{player_2_nationality}</h4>", unsafe_allow_html=True)

    #Age
    player_2_age = df.loc[df['Name'] == player_2_name,'Age'].iloc[0]
    sub_col4.markdown(f"<h4 style='text-align: left; color: black;font-size:18px'>Age: </h4>", unsafe_allow_html=True)
    sub_col5.markdown(f"<h4 style='text-align: left; color: black;font-size:18px'>{player_2_age}</h4>", unsafe_allow_html=True)

    #Height
    player_2_height = df.loc[df['Name'] == player_2_name,'Height'].iloc[0]
    sub_col4.markdown(f"<h4 style='text-align: left; color: black;font-size:18px'>Height: </h4>", unsafe_allow_html=True)
    sub_col5.markdown(f"<h4 style='text-align: left; color: black;font-size:18px'>{player_2_height}</h4>", unsafe_allow_html=True)

    #Preferred Foot
    player_2_pff = df.loc[df['Name'] == player_2_name,'PreferredFoot'].iloc[0]
    sub_col4.markdown(f"<h4 style='text-align: left; color: black;font-size:18px'>Preferred Foot: </h4>", unsafe_allow_html=True)
    sub_col5.markdown(f"<h4 style='text-align: left; color: black;font-size:18px'>{player_2_pff}</h4>", unsafe_allow_html=True)


    for i in range(24,58):  #index 24 is ballcontrol and index 57 is gkreflexes
        col_name = df.columns[i]
        col_data = df.loc[df['Name'] == player_2_name, df.columns[i]].iloc[0]
        sub_col4.markdown(f"<h4 style='text-align: left; color: black;font-size:18px'>{col_name}: </h4>", unsafe_allow_html=True)

        if col_data >=95 and col_data<=99:
            sub_col5.markdown(f"<h4 style='text-align: left; color: #C0392B;font-size:18px'>{col_data}</h4>", unsafe_allow_html=True)
        elif col_data >=90 and col_data<=94:
            sub_col5.markdown(f"<h4 style='text-align: left; color: #E67E22;font-size:18px'>{col_data}</h4>", unsafe_allow_html=True)
        elif col_data >=80 and col_data<=89:
            sub_col5.markdown(f"<h4 style='text-align: left; color: #F1C40F;font-size:18px'>{col_data}</h4>", unsafe_allow_html=True)
        elif col_data >=75 and col_data<=79:
            sub_col5.markdown(f"<h4 style='text-align: left; color: #BFF517;font-size:18px'>{col_data}</h4>", unsafe_allow_html=True)
        elif col_data >=0 and col_data<=74:
            sub_col5.markdown(f"<h4 style='text-align: left; color: grey;font-size:18px'>{col_data}</h4>", unsafe_allow_html=True)


    player_2_att = (df.loc[df['Name'] == player_2_name,'AttPosition'].iloc[0]+df.loc[df['Name'] == player_2_name,'Finishing'].iloc[0])/2
    player_2_spd = (df.loc[df['Name'] == player_2_name,'SprintSpeed'].iloc[0]+df.loc[df['Name'] == player_2_name,'Acceleration'].iloc[0])/2
    player_2_pow = df.loc[df['Name'] == player_2_name,'ShotPower'].iloc[0]
    player_2_sta = df.loc[df['Name'] == player_2_name,'Stamina'].iloc[0]
    player_2_tec = (df.loc[df['Name'] == player_2_name,'BallControl'].iloc[0]+df.loc[df['Name'] == player_2_name,'Dribbling'].iloc[0])/2

    if preferred_position_2 == "GK":
        player_2_def = (df.loc[df['Name'] == player_2_name,'GKPositioning'].iloc[0]+df.loc[df['Name'] == player_2_name,'GKDiving'].iloc[0]+df.loc[df['Name'] == player_2_name,'GKHandling'].iloc[0]+df.loc[df['Name'] == player_2_name,'GKKicking'].iloc[0]+df.loc[df['Name'] == player_2_name,'GKReflexes'].iloc[0])/5
    else:
        player_2_def = (df.loc[df['Name'] == player_2_name,'Marking'].iloc[0]+df.loc[df['Name'] == player_2_name,'SlideTackle'].iloc[0]+df.loc[df['Name'] == player_2_name,'StandTackle'].iloc[0])/3


    return player_2_att,player_2_spd,player_2_pow,player_2_def,player_2_sta,player_2_tec


def radar_chart(placeholder_1,placeholder_2,player_1_att,player_1_spd,player_1_pow,player_1_def,player_1_sta,player_1_tec,player_2_att,player_2_spd,player_2_pow,player_2_def,player_2_sta,player_2_tec):

    labels = np.array(['ATT','SPD','POW','DEF', 'STA','TEC'])

    stats_1= np.array([player_1_att,player_1_spd,player_1_pow,player_1_def,player_1_sta,player_1_tec])
    stats_2= np.array([player_2_att,player_2_spd,player_2_pow,player_2_def,player_2_sta,player_2_tec])

    angles_1=np.linspace(0, 2*np.pi, 6, endpoint=False)
    angles_2=np.linspace(0, 2*np.pi, 6, endpoint=False)
    # close the plot
    stats_1=np.concatenate((stats_1,[stats_1[0]]))
    angles_1=np.concatenate((angles_1,[angles_1[0]]))
    stats_2=np.concatenate((stats_2,[stats_2[0]]))
    angles_2=np.concatenate((angles_2,[angles_2[0]]))
    

    fig=plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles_1, stats_1, "#3498DB", linewidth=3)
    ax.fill(angles_1, stats_1, "#3498DB", alpha=0.3)
    ax.set_thetagrids(angles_1 * 180/np.pi, labels)
    ax.set_yticklabels([])
    ax.set_theta_zero_location('N')
    ax.set_ylim(0,100)
    plt.xticks(size=16)

    placeholder_1.write(fig)


    fig2=plt.figure()
    bx = fig2.add_subplot(111, polar=True)
    bx.plot(angles_2, stats_2, "#E74C3C", linewidth=3)
    bx.fill(angles_2, stats_2, "#E74C3C", alpha=0.3)
    bx.set_thetagrids(angles_2 * 180/np.pi, labels)
    bx.set_yticklabels([])
    bx.set_theta_zero_location('N')
    bx.set_ylim(0,100)

    plt.xticks(size=16)

    placeholder_2.write(fig2)



if __name__ == "__main__":


    col1,col2,col3,col4,sub_col1,sub_col2,sub_col3,sub_col4,sub_col5,sub_col6,placeholder_1,placeholder_2 = init_ui()

    player_1_att,player_1_spd,player_1_pow,player_1_def,player_1_sta,player_1_tec = select_player_1(col1,col2,sub_col2,sub_col3)

    player_2_att,player_2_spd,player_2_pow,player_2_def,player_2_sta,player_2_tec = select_player_2(col4,col3,sub_col4,sub_col5)

    radar_chart(placeholder_1,placeholder_2,player_1_att,player_1_spd,player_1_pow,player_1_def,player_1_sta,player_1_tec,player_2_att,player_2_spd,player_2_pow,player_2_def,player_2_sta,player_2_tec)

    st.write("Developed by ChunzPs")