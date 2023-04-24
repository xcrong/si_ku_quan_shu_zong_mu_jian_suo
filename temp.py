import flet as ft


bu = ["全部", "經部", "史部", "子部", "集部"]
jing_lei = ["全部", "易", "書", "詩", "禮", "春秋", "孝經", "五經總義", "四書", "樂", "小學"]
li_shu = ["全部", "周禮", "儀禮", "禮記", "三禮總義", "通禮", "雜禮書"]
xiaoxue_shu = ["全部", "訓詁", "字書", "韻書"]
shi_lei = [
    "全部",
    "編年",
    "紀事本末",
    "別史",
    "雜史",
    "詔令奏議",
    "傳記",
    "史鈔",
    "載記",
    "時令",
    "地理",
    "職官",
    "政書",
    "史評",
]
zhaolingzouyi_shu = ["全部", "詔令", "奏議"]
zhuanji_shu = ["全部", "聖賢", "名人", "總錄", "雜錄", "別錄"]
dili_shu = ["全部", "宮殿疏", "總志", "都會郡縣", "河渠", "邊防", "山川", "古跡", "雜記", "遊記", "外紀"]
zhiguan_shu = ["全部", "官制", "官箴"]
zhengshu_shu = ["全部", "通制", "典禮", "邦計", "軍政", "法令", "考工"]
mulu_shu = ["全部", "經籍", "金石"]
zi_lei = [
    "全部",
    "儒家",
    "兵家",
    "法家",
    "農家",
    "醫家",
    "天文算法",
    "術數",
    "藝術",
    "譜錄",
    "雜家",
    "類書",
    "小說",
    "釋家",
    "道家",
]
tianwensuanfa_shu = ["全部", "推步", "算書"]
shushu_shu = ["全部", "數學", "占候", "相宅相墓", "占卜", "命數相書", "陰陽五行", "雜技術"]
yishu_shu = ["全部", "書畫", "琴譜", "篆刻", "雜技"]
pulu_shu = ["全部", "器物", "食譜", "草木鳥獸蟲魚"]
zajia_shu = ["全部", "雜學", "雜考", "雜說", "雜品", "雜纂", "雜編"]
xiaoshuo_shu = ["全部", "雜事", "異聞", "瑣語"]

ji_lei = ["全部", "楚辭", "別集", "總集", "詩文評", "詞曲"]
ciqu_shu = ["全部", "詞集", "詞選", "詞話", "詞譜詞韻", "南北曲"]


def visit_view_search(e):
    print(
        bu_options.value,
        lei_options.value,
        shu_options.value,
        cunmu_options.value,
        fulu_options.value,
        visit_view_search_bar.value,
    )


def make_dropdown_from_ls(ls: list):
    return list([ft.dropdown.Option(x) for x in ls])


def set_lei_dropdown(e: ft.ControlEvent):
    bu_value = e.control.value
    if bu_value == "經部":
        lei_options.options = make_dropdown_from_ls(jing_lei)
    elif bu_value == "史部":
        lei_options.options = make_dropdown_from_ls(shi_lei)
    elif bu_value == "子部":
        lei_options.options = make_dropdown_from_ls(zi_lei)
    elif bu_value == "集部":
        lei_options.options = make_dropdown_from_ls(ji_lei)
    else:
        lei_options.options = make_dropdown_from_ls(["全部"])
    lei_options.update()


def set_shu_dropdown(e: ft.ControlEvent):
    lei_value = e.control.value
    if lei_value == "禮":
        shu_options.options = make_dropdown_from_ls(li_shu)
    elif lei_value == "小學":
        shu_options.options = make_dropdown_from_ls(xiaoxue_shu)
    elif lei_value == "詔令奏議":
        shu_options.options = make_dropdown_from_ls(zhaolingzouyi_shu)
    elif lei_value == "傳記":
        shu_options.options = make_dropdown_from_ls(zhuanji_shu)
    elif lei_value == "地理":
        shu_options.options = make_dropdown_from_ls(dili_shu)
    elif lei_value == "職官":
        shu_options.options = make_dropdown_from_ls(zhiguan_shu)
    elif lei_value == "政書":
        shu_options.options = make_dropdown_from_ls(zhengshu_shu)
    elif lei_value == "目錄":
        shu_options.options = make_dropdown_from_ls(mulu_shu)
    elif lei_value == "天文算法":
        shu_options.options = make_dropdown_from_ls(tianwensuanfa_shu)
    elif lei_value == "術數":
        shu_options.options = make_dropdown_from_ls(shushu_shu)
    elif lei_value == "藝術":
        shu_options.options = make_dropdown_from_ls(yishu_shu)
    elif lei_value == "譜錄":
        shu_options.options = make_dropdown_from_ls(pulu_shu)
    elif lei_value == "雜家":
        shu_options.options = make_dropdown_from_ls(zajia_shu)
    elif lei_value == "小說":
        shu_options.options = make_dropdown_from_ls(xiaoshuo_shu)
    elif lei_value == "詞曲":
        shu_options.options = make_dropdown_from_ls(ciqu_shu)
    else:
        shu_options.options = make_dropdown_from_ls(["全部"])
    shu_options.update()


bu_options = ft.Dropdown(
    label="部",
    options=make_dropdown_from_ls(bu),
    on_change=set_lei_dropdown,
)
lei_options = ft.Dropdown(
    label="類", options=make_dropdown_from_ls(["全部"]), on_change=set_shu_dropdown
)

shu_options = ft.Dropdown(label="屬", options=make_dropdown_from_ls(["全部"]))

cunmu_options = ft.Dropdown(
    label="是否存目", options=make_dropdown_from_ls(["全部", "是", "否"])
)

fulu_options = ft.Dropdown(
    label="是否在附錄", options=make_dropdown_from_ls(["全部", "是", "否"])
)

visit_view_search_bar = ft.TextField(hint_text="請輸入關鍵字")
visit_view_search_button = ft.FloatingActionButton(
    icon="search", text="查看", on_click=visit_view_search
)


def main(page: ft.Page):
    visit_view = ft.Column(
        [
            ft.Row([bu_options, lei_options, shu_options]),
            ft.Row(
                [
                    cunmu_options,
                    fulu_options,
                    visit_view_search_bar,
                    visit_view_search_button,
                ]
            ),
        ]
    )
    # 初始化
    bu_options.value = "全部"
    page.add(visit_view)
    page.update()


ft.app(target=main)
