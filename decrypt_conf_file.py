# -*- coding:Utf-8 -*-
import rsa
from Crypto.Cipher import AES
import os

fetslunule_key = {
    "modulus": 17234891911379545196460711219256599511638963328907075258060582079365566357448849262404189521484100167389577810564169590174720621556550140712958854132782273617176444571926504839475816836990924976043287184218511398967425218719462272087905784406620462836589302749283496951258084526489985617828558348283578560292773093247850424928137910587000073201458966200659342152873868442004157642719690370058948037997596310903447699356668758825442779517157606349714931352523379499698854749548544882981699026971514856746487018643205780185154634123759878798994662127928332464975241742736958586881607000196220059189883895082961804560083,
    "publicExponent": 65537,
    "privateExponent": 4596619859300899804521671291047593006453414712696137577790269834829649424933219956018170325862041088633938546940676568452384786367806581160593371856919013085045502154091633399288917748657466433560593507376830809200171283366609412298770239798027359658219699143304183029602210345888863674169177279546647995107385046067448150741691042317619206774732138998654907898552132866126966868293047846641500316145270913544905182231613283686953702218717750552101620336002961142431090248993988510579720944160590061351866360770566497525338076021394765953725638227560156333048268690142639932293639310825637663538930206341637028568729,
    "primeP": 161323775474857892828789901536400187924118372668508776015696670677619702415583827201907316852982345636434358425619189192900941687174841164900107048769849247278178684242025006794566893583409460088264057745457693558380731752766369037136671212014849038053754678638698682372473028722205854623235559933102924535167,
    "primeQ": 106834171594661081981937186990650850046078816328455726683039804545656445520567626137319557507528327587944119126985276881704559821623864908306792267560037238432097677050954625436907777449402332935054262126616068300892473901736185183259835842991121415422866711339052098414492429418987283384036690718720603160749,
    "primeExponentP": 59567481616736898981703264221422221761382737998462606936598314444172287085992844262919498306686601187971299259068293624654926040068113910453906807958581899307027266734405956016017276619694608002745043767373098042621043497340332397419325063087222971327079504224756540804911345072991737126015492238295278557555,
    "primeExponentQ": 6055952324246851695422382008182674030260506319486900905251886322033564171520038010591607124837385553034353152520718122824243400481142837395055209637083454243789658822410187123275590784206321114084053035695541354316119757464484611071765417347635931737735169944070960611713068576400167199775642858538642915333,
    "crtCoefficient": 8601648518134999738864632685663153611144580321439230342612388432991486717800141732809341352910547166814371685059633786820545703989449037918037999223057608461031034095286082090110685881993895594609382869569458081513874989681276524937525087003018720827779095352023602066995149512476859362349080098843043421209
    }

recashMgt_key = {
    "modulus": 19524245934644411653193953695685840325355244321728924384185513933322840027259067762890211922689051427109140287274367762627181143650754594781295095691099020983518711480003505080099768428205585029666551199156486183427004004499568685901400335855319222962671452816446078551428707142584427323966169316021383907160511812826201093728390027359674763170099804242656741865952274953749870357993151261727576487041431838646944912915258429116645605785982816142521229974123532097321615900098439443164589373045919176721633445563601176512088261189660312074423176074673043878060036608131304352484371162475605995925483090103991475446409,
    "publicExponent": 65537,
    "privateExponent": 14926275143254786716816098723086922773719788916971852517216943171052600117273617530922811357896906230868810836829693883011270836936902169191864567792409390853063735008966165906712829356827203362091386769784052172791601410461905333929198178545845232892850264743006208304655881623585265761519095796887550511931414632085411578483274237218233946140290132483626580391822766107017407968839178533077393772915829184223315325346127698604759529961687496033739447775485062489459897640792210462007889584130549759337915956157830906863432998145649089558652965702959975778616237643878081751237019049336257843320650599444195766840477,
    "primeP": 141333172349390822277606830026484929601154584784107358700045777642656211329291134792127898353725081944131740152213719361235168419316559562339631797497709034067831145024040877299415384893180476825879080926151455652432915058133528955689770876175758981003749421368563614338228854264947454608366130747952787760027,
    "primeQ": 138143406888075597201902505350369368850356889387010909086677764902298950890887579936403507642964979834293992729729918556078554742888969240837004262848912691185579025185986753226987458899723120434863838746469856518022940896882063592847940989270533353173238936820864129343864651456565367700657299539775031389867,
    "primeExponentP": 7457315867131444274775537760831055534443025377778098576144136885855397390431187636162446747748315201532074361755268650550852379480242656309724991314022275047783085882678995890891838212927324852585407660445728880573004871614900638246719069988186437528586378673001403457308014984637507027110335842751739323957,
    "primeExponentQ": 93330113169405423154990878883658155615717106235999237402243486833072777951322602146026490500138248807895312817099525518523737253015775685132673722418806280843247058885208896846534380849032464157566965045355231961311957430020402668729546411674800574918771082069936082746514109167986706527335753112327678484659,
    "crtCoefficient": 14636755527037687921531055122769929579537932389096555478940209788998096283717674949660718729584008421147218441787549010844809690518915126943765989147530875529426281097218081411382547698544664770433731155868970398450806152752471699085651369253207168689847370686663233532645705665905548581466825856540320774248
    }

private_key_fetslunule = rsa.PrivateKey(fetslunule_key["modulus"], fetslunule_key["publicExponent"],
                                        fetslunule_key["privateExponent"], fetslunule_key["primeP"],
                                        fetslunule_key["primeQ"],
                                        fetslunule_key["primeExponentP"], fetslunule_key["primeExponentQ"],
                                        fetslunule_key["crtCoefficient"])

private_key_recashMgt = rsa.PrivateKey(recashMgt_key["modulus"], recashMgt_key["publicExponent"],
                                       recashMgt_key["privateExponent"], recashMgt_key["primeP"],
                                       recashMgt_key["primeQ"],
                                       recashMgt_key["primeExponentP"], recashMgt_key["primeExponentQ"],
                                       recashMgt_key["crtCoefficient"])
def decrypt_conf_file() :
    # Déchiffrement du fichier de configuration
    path_aes_key = "./results_decrypted_4/crypted/FrateTng.tar"
    path_conf_file  = "./results_decrypted_4/crypted/ShirtsYrs.tar"
    with open(path_aes_key, "rb") as f :
        content = f.read()
        aes_key = rsa.decrypt(content, private_key_fetslunule)
        cipher = AES.new(aes_key, AES.MODE_ECB)
        with open(path_conf_file, "rb") as f2 :
            print cipher.decrypt(f2.read())


