import flet as ft
import sqlite3


def main(page: ft.Page):
    ##### -------------------------- Data -------------------------- ####

    no_result = (
        "查無此書",
        "",
        "",
        None,
        "",
        "",
        None,
        "",
        "",
        "",
        "",
        "",
        "",
    )

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

    ##### -------------------------- Funcion -------------------------- ####
    def main_view_show_search_results(e):
        keyword = main_view_search_bar.value
        if not keyword:
            return None
        main_view_items_lv.controls = []
        for result in main_view_get_results(keyword):
            main_view_items_lv.controls.append(make_item(result))
        main_view_search_bar.focus()
        main_view_items_lv.update()

    def visit_view_show_search_results(e):
        # visit_view_items_lv.controls = []
        # for result in visit_view_get_results(e):
        #     print(result)
        #     visit_view_items_lv.controls.append(make_item(result))
        # visit_view_items_lv.update()
        pass

    def on_keyboard(e: ft.KeyboardEvent):
        print(e.key)
        if e.key == "Enter":
            if main_view.visible:
                main_view_show_search_results(None)
            elif visit_view.visible:
                visit_view_show_search_results(None)

    def main_view_get_results(keyword: str):
        with sqlite3.connect("data.db") as conn:
            c = conn.cursor()
            c.execute(
                "SELECT * from items where title like ? or title_sim like ? or title_jp like ? or title_jp_sim like ?",
                (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"),
            )
            results = c.fetchall()
            if len(results) > 0:
                return results
            return [no_result]

    def make_item(result: tuple):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                f"序號：{result[0]}", size=24, color=ft.colors.RED_ACCENT
                            )
                        ]
                        + list(
                            [
                                ft.Text(x, size=18, color=ft.colors.BLUE)
                                for x in result[1:7]
                            ]
                        ),
                    ),
                    ft.Text(f"繁體書名：{result[7]}", size=18, color=ft.colors.BLUE),
                    ft.Text(f"簡體書名：{result[8]}", size=18, color=ft.colors.BLUE),
                    ft.Text(f"提要：", size=18, color=ft.colors.BLUE),
                    ft.Text(result[11], width=int(page.window_width * 0.8), size=16),
                ],
            ),
            expand=0,
            width=int(page.window_width * 0.8),
        )

    def switch(e: ft.ControlEvent):
        signal = e.control.selected_index
        if signal == 0:
            main_view.visible = True
            visit_view.visible = False
            doc_view.visible = False
            dif_view.visible = False
        elif signal == 1:
            main_view.visible = False
            visit_view.visible = True
            doc_view.visible = False
            dif_view.visible = False
        elif signal == 2:
            main_view.visible = False
            visit_view.visible = False
            doc_view.visible = True
            dif_view.visible = False
        elif signal == 3:
            main_view.visible = False
            visit_view.visible = False
            doc_view.visible = False
            dif_view.visible = True

        else:
            if page.theme_mode == "dark":
                page.theme_mode = "light"
                with open("config", "w", encoding="utf8") as fi:
                    fi.write("light")
            else:
                page.theme_mode = "dark"
                with open("config", "w", encoding="utf8") as fi:
                    fi.write("dark")
        page.update()

    def show_dif_table():
        lv = ft.ListView(spacing=1, expand=True, padding=5)

        with open("dif.md", "r", encoding="utf8") as fi:
            for line in fi:
                lv.controls.append(ft.Text(line.replace("|", "\t"), size=24))
        dif_lv = lv
        return dif_lv

    def visit_view_get_results(e):
        print(
            bu_options.value,
            lei_options.value,
            shu_options.value,
            cunmu_options.value,
            fulu_options.value,
            visit_view_search_bar.value,
        )
        if bu_options.value == "全部" or bu_options.value == None:
            bu_options.value = ""
        if lei_options.value == "全部" or lei_options.value == None:
            lei_options.value = ""
        if shu_options.value == "全部" or shu_options.value == None:
            shu_options.value = ""
        if cunmu_options.value == "全部" or cunmu_options.value == None:
            cunmu_options.value = ""
        if fulu_options.value == "全部" or fulu_options.value == None:
            fulu_options.value = ""
        with sqlite3.connect("data.db") as conn:
            c = conn.cursor()
            c.execute(
                "select * from items where bu like ? and lei like ? and shu like ? and cunmu like ? and fulu like ? and title like ? or title_sim like ? or title_jp like ? or title_jp_sim like ?",
                (
                    f"%{bu_options.value}%",
                    f"%{lei_options.value}%",
                    f"%{shu_options.value}%",
                    f"%{cunmu_options.value}%",
                    f"%{fulu_options.value}%",
                    f"%{visit_view_search_bar.value}%",
                    f"%{visit_view_search_bar.value}%",
                    f"%{visit_view_search_bar.value}%",
                    f"%{visit_view_search_bar.value}%",
                ),
            )
            # print(c.fetchall())
            if c.fetchall():
                return c.fetchall()
            else:
                return [no_result]

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

    ##### -------------------------- Controls -------------------------- ####

    rail = ft.NavigationRail(
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.SEARCH,
                label="搜索",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                label="瀏覽",
            ),
            ft.NavigationRailDestination(icon=ft.icons.DOCUMENT_SCANNER, label="說明"),
            ft.NavigationRailDestination(icon=ft.icons.ATTACH_FILE, label="附件"),
            ft.NavigationRailDestination(
                icon=ft.icons.SWITCH_ACCESS_SHORTCUT_OUTLINED, label="主題切換"
            ),
        ],
        on_change=switch,
    )

    ### ----------- Mian View ---------- ###
    main_view_search_bar = ft.TextField(hint_text="請輸入書名，繁簡均支持~", expand=0,autofocus=True,filled=True)
    main_view_search_button = ft.FloatingActionButton(
        icon=ft.icons.SEARCH_OUTLINED, text="搜索", on_click=main_view_show_search_results
    )

    main_view_items_lv = ft.ListView(spacing=0, expand=1)
    ### ---------- Visit View ---------- ###
    # visit_view_search_bar = ft.TextField(hint_text="搜索", expand=0)
    # visit_view_search_button = ft.FloatingActionButton(
    #     icon=ft.icons.SEARCH_OUTLINED,
    #     text="搜索",
    #     on_click=visit_view_show_search_results,
    # )

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
        icon="search", text="查看", on_click=visit_view_show_search_results
    )
    visit_view_items_lv = ft.ListView(spacing=0, expand=1)

    ##### -------------------------- View -------------------------- ####

    main_view = ft.Row(
        [
            rail,
            ft.VerticalDivider(width=1),
            ft.Column(
                [
                    ft.Row(
                        [main_view_search_bar, main_view_search_button],
                        alignment="spaceBetween",
                    ),
                    main_view_items_lv,
                ]
            ),
        ],
        expand=True,
        visible=True,
    )

    visit_view = ft.Row(
        [
            rail,
            ft.VerticalDivider(width=1),
            ft.Column(
                [
                    ft.Text("此處尚未開發完成，後面的邏輯還在思考中，待日後更新.....", size=24, color="red"),
                    ft.Row([bu_options, lei_options, shu_options]),
                    ft.Row(
                        [
                            cunmu_options,
                            fulu_options,
                            visit_view_search_bar,
                            visit_view_search_button,
                        ]
                    ),
                    visit_view_items_lv,
                ]
            ),
        ],
        visible=False,
        expand=True,
        alignment=ft.MainAxisAlignment.START,
    )

    doc_view = ft.Row(
        [
            rail,
            ft.VerticalDivider(width=1),
            ft.Column(
                [
                    ft.Markdown(
                        open("doc.md", "r", encoding="utf8").read(),
                        selectable=True,
                        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                        on_tap_link=lambda e: page.launch_url(e.data),
                    ),
                ]
            ),
        ],
        visible=False,
        expand=True,
        alignment=ft.MainAxisAlignment.START,
    )

    dif_view = ft.Row(
        [rail, ft.VerticalDivider(width=1), show_dif_table()],
        visible=False,
        expand=True,
        alignment=ft.MainAxisAlignment.START,
    )

    ##### --------------------- Add to Page --------------------- ####

    page.add(
        ft.Row([main_view, visit_view, doc_view, dif_view], expand=True),
    )
    page.on_keyboard_event = on_keyboard
    page.theme_mode = open("config", "r", encoding="utf8").read().strip()
    page.update()


##### ---------------------- Run App ---------------------- ####

ft.app(target=main)
