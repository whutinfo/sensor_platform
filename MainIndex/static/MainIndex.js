
///添加Tab
function AddTabMenu(tabid, url, name, img, Isclose, IsReplace)
{
    var id = "tabs_" + tabid;
    //var imgsrc = "../Themes/Images/32/" + img;
    var icon = "icon" + " " + "icon-" + img;


    if (IsReplace == "true")
    {
        $("#tt_main").tabs('close', name);
    }
    if ($("#tt_main").tabs('exists', name))  //tab存在 直接选中
    {
        $("#tt_main").tabs('select', name);

        
    }
    else   //tab 不存在就添加
    {
        var content = '<iframe scrolling="auto" frameborder="0"  src="' + url + '" style="width:100%;height:95%;"></iframe>';
        $("#tt_main").tabs('add', {
            title: name,            
            closable: Isclose,
            //icon: 'icon icon-add',
            icon:icon,
            content: content,
        })
    }

}