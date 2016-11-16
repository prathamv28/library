tinyMCE.init({
        mode : "specific_textareas", // only specific textareas
                editor_selector : "mceEditor", // specified by the mceEditor class
        theme : "advanced",
        plugins : "table,save,advhr,advimage,advlink",
        theme_advanced_buttons1 : "bold,italic,underline,strikethrough,sub,sup,removeformat,charmap,separator,justifyleft,justifycenter,justifyright,bullist,numlist,outdent,indent,separator,formatselect,styleselect,code",
        theme_advanced_buttons2 : "cut,copy,paste,separator,search,replace,image,link,anchor,separator,tablecontrols",
        theme_advanced_buttons3 : "",
        theme_advanced_toolbar_location : "top",
        theme_advanced_toolbar_align : "left",
        theme_advanced_path_location : "bottom",
        theme_advanced_styles : "Left=left;Right=right;", // possible classes
        content_css : "/media/js/tmce.css", // add css styles
        plugin_insertdate_dateFormat : "%Y-%m-%d",
        plugin_insertdate_timeFormat : "%H:%M:%S",
        extended_valid_elements : "a[name|href|target|title|onclick],img[class|src|border=0|alt|title|hspace|vspace|width|height|align|onmouseover|onmouseout|name],hr[class|width|size|noshade],font[face|size|color|style],span[class|align|style]",
        width : "640", height : "350" // set size of field
    })