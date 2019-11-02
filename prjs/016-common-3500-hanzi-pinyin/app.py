# coding:gbk
import json
from pypinyin import lazy_pinyin

def main():
    text = 'һ�������������²���ؤ��ר�������ҵ�Զ�˿������ɥ���зᴮ���赤Ϊ�������˾�ô��֮��է������ƹ���ǹԳ��Ҿ���Ҳϰ����������Ǭ�������¶��ڿ��ƻ��微��Щ���������Ķ����ͤ��������ʲ�ʽ��ͳ����Դ��ز������̸��ɴ������������ټ����ηݷ���������������Ż��ɡΰ������α�������������Ƶ赫λ��ס������������Ӷ���ʹֶ�����̹������½����������ֱ�ٶ��������׷����������޸��㰳�������Ⱥ��н賫��ծֵ�����ƫ��ͣ��ż͵�����������߰�ɵ����ɮ��Ƨ���ܶ���Ԫ�ֳ����ȹ������õ�������ȫ�˹����������˱���ߵ������޼��ڸԲ���ð����д��ũ��ԩ����������ұ�䶳����׼�������������������ƾ���˵���͹���������䵶���з��п��̻�������մ���ɾ��������ε���ˢȯɲ�̹̿�������ǰ�����ʰ���ʣ�����������Ȱ�칦�����Ӷ���Ŭ���������Ʋ�����ѫ�տ�ļ���׹����Ȱ�����ذ�����׽�ϻ��ƥ��ҽ����ʮǧ����뻪Э����׿�����ϲ���ռ��¬±������ӡΣ��ȴ�Ѿ�ж�䳧������ѹ������ԭ���ó�ȥ�������ֲ漰��˫������ȡ�ܱ����ѵ��ڹž���߶ֻ���ٰȶ���̨ʷ��Ҷ��˾̾��ߴ���Ը�ߺ�ϼ���ͬ������������������������ͷ�ɶַԺ�����˱��֨�ⳳ�����Ǻ�ѽ���ʸ���ŻԱǺ������ζ��������غ�ӽ���乾����������ҧ�ۿ����ʰ�Ʒ��߹��찥�ƻ�Ӵ�������Ŀ����ܲ��������������뻽����Ψ���ٿ����̰���ơɶ��?Х��ι����������ϲ������������ɤ�������������Ҽ�������˻�ں���ج�뺿���½������Ļ����Ŷ�԰����Χ�̹�ͼ��ԲȦ��ʥ�ڵس���ַ�����������ӿ��̳�����׹����̹ƺ��������¢���ݶ⹸�ѵ�幡�����������öѶ鱤�̿��߶��������������Ĺǽ��ī�ձں���ʿ׳���Ǻ�Ҽ��������Ϧ���ҹ������̫��ز�뺻ʧͷ�Ŀ�ж������η���������Ƚ��׵��ݰ�Ůū�̼���������ױ����ʼ������׷�����ķ�ʼ�����ίҦ��������������¦����������Ȣ�����Ӥ����ý��ϱ��ɩ���ӵ������ӿ����ִ���Т�ϼ���ѧ����������լ���ذ�������ڹ��涨���˱�ʵ��������һ��ܹ��׺��������ݿ����޼ż��ܸܿ���Ԣ��į�����կ�����Ѱ���ٷ��佫ξ��С�ٶ��⳾�г��Ⱦ�ʬ���ᾡβ���ƨ����������ʺ��мչ����������ɽ���������᫸ڵ���������Ͽ���ͷ��������±�ոǶΡ����Ѳ�������ɾ޹��ײ�Ѱ�������в�˧��ʦϣ�����������ĵ۴�ϯ�ﳣñ�����Ļ����ƽ�겢�һ����Ĺ�ׯ��Ӵ���®��Ӧ�׵������ӷ϶���ͥ������ӹ��������͢��������Ū��ʽ�����ڵ������һ�������ǿ�鵱¼��ͮ�ʱ������Ӱ�۳������������ܻ�����ͽ��������ѭ΢�»��ı������־��æ���ǿ������޻�̬��ŭ���²���˼������Թ�����������пֺ�ˡ�����޶���Ϣǡ�Ҷ�����Ϥ�������ƻ�����������㲵��龪�����ϧ�ݵ��ҳͱ��ѹ߶�����ǳ���������޸з���Ը�Ȼ���Ľ���ۿ�ο������㾺�����и����ų��Ϸ���ҽ��ս�ݽش��������������ֲ����˰Ǵ����п���ִ��ɨ��Ť�糶�Ű�������ҳм���������ץͶ�����۸��׿�����������̧����ĨѺ���������Ĵ�����Ĺվ��ذ����־�׾�а���£��ӵ��š������������ȭ˩��ƴʰ�óֹ�ָ��������ֿЮ�ӵ������Ӱ�Ų����ͦ����ͱ��׽�ƺ�����貶����񻻵����ݴ��������Ƶ��ڵ���������Ҵ����̽�ӿ����ڴ������������������Ҿ�մ�������Ԯ�����§������ɦ�Ѹ��°��Я���ҡ̯ˤժ��Ħ��ġƲ����˺ײ�����˲���׫�캳���ò����ܲ�������֧�ոĹ�������Ч�����Ƚ�������ɢ�ؾ�����������ի�߶���б���⸫ն��˹�·�ʩ�����������޼��յ���ּ��Ѯ��ʱ���������������������ӳ���������������Իν���ɹ��������޳��վ����羧������Ͼ��ů��ĺ�����������������������������������ľδĩ�������Ӷ����ɱ��Ȩ���ɼ���ӲĴ��ȶ���������������ɰ弫����������ö��֦����ǹ��ݼܼϱ���ĳ����Ⱦ����������������դ��ջ������˨����У�����˸����Թ���Φ����ͩɣ�����뽰׮Ͱ��÷��������������е�����������ؼ�����ɭ��ù���ֲ׵����Ҭ��Ш����鹿�¥���������黰�ե�񻱲۷���ģ��ӣ���ٳ����̴������Ƿ�λ���ŷ���ۿ�ЪǸ��ֹ���˲��������������ѳ���ֳŹ��������ĸÿ���ȱϱ�ëձ��̺����å��������������ˮ��֭��㺺��Ѵ������������̭�����������ɳ�湵û���ٲ׻�ĭ�ںӷ������ӹ�մ��йȪ���ڷ���Ţ�ݲ�����ע��̩Ӿ��к���������ϴ�嶴����޻���Ǣ����ǳ�����ǲ�û�Ũ���ֺ��˸�ԡ����Ϳ����ӿ���������л�������ɬ����Һ�������������Ե����������������Ԩ���������������¸ۿ������Ⱥ�����ʪ������Դ����Ϫ�������̻����Ϲ��������ı�̲��Ư��©����Į����������Ǳ��̶���γ�������ļ����ٹ����ƻ���������ֲ�¯���׳����ž�̿��ը����˸���Һ������̿����������뺸�����ٽ���Ȼ�ͼ�ɷú����Ϩ��Ѭ�����찾ȼ�����ﱬצ��������ү�ֵ�ˬƬ�������ţĵ��������ǣ����Ϭ��Ȯ��״�̿񱷺������ݽƶ���ʨ���������Բ��Ͳ�����è��׺ﻫԳ��������������õ�������貣ɺ�������������������������ɪ����赹�ư��ȿ����ƿ�ɸ�����������˦�����ɼ�����е黭����η���������跬����������Ƹ���ű���ߴ���ƣ���ۼ���֢Ȭ���۶�ʹ����̵�ձ������ݴ��̱ȳ񫰩�Ѣ�ǰװ����ĽԻ�Ƥ��������ӯ��յ�μ�п��ǵ���ʢ��Ŀ��äֱ�����ζ�ʡü������գ�п�����������˯�����Ƕ���Ϲ���Ƶ�˲?ͫհ��ìʸ֪�ؽö̰�ʯ������ɰ������ש��������������˶����Ӳȷ���µ���鱮����������̼����Ű���ĥ�׻ǽ�ʾ��������ף��������Ʊ���������������ݺ���˽ͺ�ѱ����ֿ���������������������ƽ��ƻ�ϡ����˰�ɳ��ȵ��ڻ�������Ѩ����մ�ͻ��խ��Ҥ�ϽѴ������ѿ߿�������վ�����¿�ͯ�߶���Ͱ���Ц���ϵ��Է��������Ƚ����Ͳ���ɸ�ݿ��ǩ�򹿻�����������ƪ¨�ݴ�������������������ѷ�����ճ������������⾫�����ǲ����㿷Ŵϵ����������������������Լ������γ��ɴ�����ݷ�ֽ�Ʒ�Ŧ��������ϸ֯�հ����ﾭ���޽��ƻ�������ͳ����̼���������ά�����������׺���¶л����Ʊ�Ե�������ӧ�����ֽɸ�ȱ�������޷���������������������Ⱥ�����̳������̴��溲����ҫ�Ͽ��߶�ˣ�͸����ŰҶ��ʳܵ���������ְ��Ƹ�۴����������߼�Ф��Ǹظγ���֫���ʼ緾�������ȷ�������вθ����̥����ʤ�����ʿ��ȸ콺����֬������������ŧ���Ÿ�����Ƣ��Ҹ�縯ǻ�����������������Ȱ򲲸����Ĥϥ�����α������Գ����¾�Ҩ���������������ۺ��㽢�ն沰�ϴ�ͧ������ɫ���հ�������âܽ��֥��«�Ұ�о������ѿέ����̦�����������ɻӢƻ��ï����é�Ծ���ã��������׾��ݼ�������������ٻ�ӫҩ��ݩ��Ī������Өݺç���վ��˲����������Ƽή��өӪ�����������϶�����п��ٽ��������������ر�����������ε���߰��ν������ٱ�ޱѦн������ź����Ģպ��²Ű�����ʭ����Ϻʴ�����ð������������������ȵ����������Ӽ���������������֩������Ӭ����Ы�������������������з���Ѫ�������ν��ú��²���������˥��Ԭ������̻���౻Ϯ������װ��ԣȹ��������Ӻְ����ʽ���Ҫ�����۹����������ǽⴥ�������ľ�Ʃ�ƶ��ϼ�����ѵ��Ѷ�ǽ������������Ϸ���þ�֤����ʶթ���������ʫ�ϻ�����ѯ������������ջ�˵������ŵ���̿�˭����׻̸��ı����г��ν����лҥ��ǫ����̷��Ǵ�Ȼ��������ԥ����ò���긺�������Ͱ��˻��ʷ�̰ƶ�Ṻ���ᷡ�������ó�Ѻ����ֻ���¸�����޸������ʹ�����׸׬��������Ӯ������߸��Ը���ó�Խ����Ȥ��ſֺԾ�ϵ����˾�����·�����ζ�ӻ̤�߲��������㵸̣�ĵŲ���������������ɳ�������ת�����������ؽνϸ������Է�����ԯϽ�������Ǳ������賽����ɴ�Ǩ����Ѹ����ӭ�˽��������ԶΥ���������Լ�׷����������ѡѷ͸���;��ͨ���ų����������߱��������������ǲң����������ص����ǰ�а����������֣����������������ͺ����ҳ꽴�Ϳ����������Ѳ�������Ұ������붤���ƶ۳����Ƹ�Կ�վ���ťǮǯ�������Ǧí����ͭ��աϳ����������������������ﱷ�п���ê���സ׶���Ƕ��������¶Ͷ������侵�����ⳤ�������ʴ����м���բ�ֹ������������ֲ����������������谢����½��ªİ�����¶�Ժ����������������¡��������϶��������ȸ�����ż��ʹƳ�����ѩ�����ױ�������ù����˪ϼ¶�����ྸ���ǿ������ѥ��Ь���ϱ��ͺ�������ҳ������˳����˶ٰ���Ԥ­���ľ���Ƶ��ӱ�����ն�߲����Ʈ��ʳ�ͼ������α��Ƕ��Ľȱ������ڹݲ���������������ѱ������¿ʻ��פ�ռ���溧�鿥��ƭɧ���������޹�������κħ��³�����꾨����������𯼦��ŸѻѼ��ԧ�Ҹ������ȵ������ӥ¹������������ǭĬ����������������'
    d = {char: lazy_pinyin(char)[0] for char in text}
    print(json.dumps(d, ensure_ascii=False))


if __name__ == '__main__':
    main()