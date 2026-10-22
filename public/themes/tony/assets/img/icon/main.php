


<?php
/**
 * Yii view main
 *
 * @author luubk
 * @since Feb 21, 2013 - 11:03:34 AM
 */
$controller = Yii::app()->controller->id;
$action = Yii::app()->controller->action->id;
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset='utf-8'>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!--<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />-->
        <title><?php echo $this->pageTitle; ?></title>
        <link rel="shortcut icon" href="<?php echo $this->assets ?>/img/logo khong chu.png" />
        <link href="<?php echo $this->assets ?>css/style.css" type="text/css" rel="stylesheet">
        <link href="<?php echo $this->assets ?>css/repon.css" type="text/css" rel="stylesheet" media="all">
        <link href="<?php echo $this->assets ?>css/re_slide.css" type="text/css" rel="stylesheet">
        <link href="<?php echo $this->assets ?>css/jquery.datepick.css" rel="stylesheet" media="screen">
        <link href="<?php echo $this->assets ?>css/colorbox.css" rel="stylesheet" media="screen" /> 
        <link href="<?php echo $this->assets ?>css/jquery-ui.css" rel="stylesheet" media="screen" /> 
        <link rel="stylesheet" href="<?php echo $this->assets ?>css/slidorion.css" /> 
        <script language="JavaScript">
            <!--
           var dictionaries = "ev_ve";
            // -->
        </script> 
        <script language='javascript' src="<?php echo $this->assets ?>js/autosearch.js" charset="utf-8"></script>
        <!--slide-->
        <script>document.documentElement.className = "js";</script>
        <script type="text/javascript" src="<?php echo $this->assets ?>js/jquery.min.js"></script>
        <script type="text/javascript" src="<?php echo $this->assets ?>js/jquery-ui.js"></script>
        <script type="text/javascript" src="<?php echo $this->assets ?>js/jquery.yiiactiveform.js"></script>

        <script src="<?php echo $this->assets ?>js/sdb.js" type="text/javascript"></script>
        <script src="<?php echo $this->assets ?>js/show_hide_menu.js"></script>
        <script src="<?php echo $this->assets ?>js/col/jquery.easing.js"></script>
        <script src="<?php echo $this->assets ?>js/col/jquery.slidorion.min.js"></script>
        <script src="<?php echo $this->assets ?>js/jcarousellite.js"></script>
        <script language="javascript" type="text/javascript" src="<?php echo $this->assets ?>js/jquery.cycle.all.2.74.js"></script>
        <script src="http://maps.googleapis.com/maps/api/js?sensor=false" type="text/javascript"></script>
        <script language="javascript" type="text/javascript" src="<?php echo $this->assets ?>js/gmap3v5.1.1/gmap3.js"></script>
        <script type="text/javascript" src="<?php echo $this->assets ?>js/bootstrap.js"></script>
        <script type="text/javascript" src="<?php echo $this->assets ?>js/jquery.datepick.js"></script>
        <script type="text/javascript" src="<?php echo $this->assets ?>js/json_sans_eval.js"></script>
        <script type="text/javascript" src="<?php echo $this->assets ?>js/ColorBox/jquery.colorbox-min.js"></script>
        <script type="text/javascript" src="<?php echo $this->assets ?>js/jquery.IEplaceholder.js"></script>
        <script type="text/javascript" src="<?php echo $this->assets ?>js/jquery.autosize-min.js"></script>
        <script type="text/javascript" src="<?php echo $this->assets ?>js/functions.js"></script>
        <script type="text/javascript" src="<?php echo $this->assets; ?>js/tiny_mce/tiny_mce.js"></script>
        <script type="text/javascript" src="<?php echo $this->assets ?>js/jcarousellite.js"></script>
        <script type="text/javascript" src="<?php echo $this->assets ?>js/jRating/jquery/jRating.jquery.js"></script>       
        <link rel="stylesheet" href="<?php echo $this->assets ?>js/jRating/jquery/jRating.jquery.css" type="text/css" />
        <!-- glDatePicker -->
        <script language="javascript" type="text/javascript" src="<?php echo $this->assets ?>js/glDatePicker/lang/<?= $this->lang ?>.js"></script>
        <script language="javascript" type="text/javascript" src="<?php echo $this->assets ?>js/glDatePicker/glDatePicker.js"></script>
        <link media="all" type="text/css" rel="stylesheet" href="<?php echo $this->assets ?>js/glDatePicker/css/glDatePicker.cus.css" />
        <!-- //glDatePicker -->
        <!-- scrollbar -->
        <script language="javascript" type="text/javascript" src="<?php echo $this->assets ?>js/scrollbar/jquery.jscrollpane.min.js"></script>
        <link media="all" type="text/css" rel="stylesheet" href="<?php echo $this->assets ?>js/scrollbar/jquery.jscrollpane.css" />

        <link media="all" type="text/css" rel="stylesheet" href="<?php echo $this->assets ?>css/default.css" />
        <script src="<?php echo $this->assets ?>js/cse.js" type="text/javascript"></script>
        <!--tu dien-->
        <!--<script type='text/javascript' src='http://1tudien.com/js/1tudien_widget.js'></script>-->
        <!--[if gte IE 7]>
         <link href="<?php echo $this->assets ?>css/repon.css" type="text/css" rel="stylesheet">
        <link href="<?php echo $this->assets ?>css/ie8.css" media="all" type="text/css" rel="stylesheet" />
        <style>
            .btn {
                border-radius:10px;  
                behavior:url(<?php echo $this->assets ?>css/IE/PIE.htc);
                zoom:1;
                position:relative; 
            }
            input {
                border-radius:10px;  
                behavior:url(<?php echo $this->assets ?>css/IE/PIE.htc);
                zoom:1;
                position:relative; 
            }
        </style>
        <![endif]-->
        <!--[if IE 7]>
         <link href="<?php echo $this->assets ?>css/repon.css" type="text/css" rel="stylesheet">
        <link href="<?php echo $this->assets ?>css/ie7.css" media="all" type="text/css" rel="stylesheet" />
        <![endif]-->
        <!--[if gte 
        IE 7]>
        <script type="text/javascript">
        $(function(){
            $(".breadcrumb>ul>li:last-child").css("display","none")
            $(".menu_left>ul>li:last-child").css("border","none")
            $(".colleft,.menu_left").removeAttr('style')
            //$(".colleft").css('margin-left','-41px')
         })
        </script>
      <![endif]-->
        <!--[if IE 7]>
        <script type="text/javascript">
        $(function(){
            $(".colleft,.menu_left").removeAttr('style')
         })
        </script>
        <![endif]-->
        <!--[if lt IE 9]>
        <link href="<?php echo $this->assets ?>css/ie.css" media="all" type="text/css" rel="stylesheet" />
        <script>
                document.execCommand("BackgroundImageCache", false, true);
        </script>
        <![endif]-->
        <!--[if lt IE 9]>
         <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
         <![endif]-->
        <script>
            function bindInOut(element, value)
            {
                element.focus(function()
                {
                    if (element.val() == value)
                        element.val('');
                }).
                        blur(function()
                {
                    if (element.val() == '')
                        element.val(value);
                });

                element.blur();
            }
            bindInOut($('.inp_txt'), 'Here your value :)');
        </script>

    </head>
   
    <body id="body" onload='popuplogin()'
    <?php
    if (isset($this->userModel)) {
        $id = $this->userModel->user_id;
        $user = User::model()->findByAttributes(array('user_id' => $id));
        $curent_mail = $this->userModel->user_email;
        $newMess = Message::model()->findAllByAttributes(array('message_to' => $curent_mail, 'message_readed' => 0, 'delete_to' => 0, 'message_save' => 0));
    }
    if (isset($user)) {
        $user_openwindow_newmess = $user->user_openwindow_newmess;
    }

    if (isset($newMess) && $newMess != "") {
        $count = count($newMess);
    }
    $act = Yii::app()->controller->id;
    if (isset($this->i) && $this->i >= 5) {
        echo "onload='hide_otherstep($this->i ,0,0)'";
    } elseif (isset($user_openwindow_newmess) && $user_openwindow_newmess == 1) {
        if (isset($count) && $count != "" && $act != "user") {
            echo "onload='newmess()'";
        }
    }
    elseif(isset(Yii::app()->session['change_pass'])){
           echo "";
    }
    ?>
          >  
              <?php
              //$model = new Options()
              $obj_webconfig = Options::model()->findAllByAttributes(array('language' => $this->lang));
              $arr_webconfig = array();
              $sender_info = array();
              if ($obj_webconfig != NULL && !empty($obj_webconfig)) {
                  foreach ($obj_webconfig as $webconfig) {
                      $cname = $webconfig->option_key;
                      $arr_webconfig[$cname] = $webconfig->option_value;
                  }
              }
              ?>
        <!--header-->
        <!--top header-->
        
       
        <div class="header-re">
            <div class="top-re">
                <div class="icon-menu-re fl"></div>
                <div class="login-re fl">
                    <a  id="login"><?php echo Yii::t('main', 'Login') ?></a>
                    <!--<a  id="login" href="<?php //echo $this->createUrl("user/login/lang/$this->lang")    ?>"><?php echo Yii::t('main', 'Login') ?></a>-->
                </div>
                <div class="icon-search-re flrg">
                    <div class="btn-search-re"></div>
                    <div class="box-search-re"></div>
                </div>
            </div>
            <div id="menu-re"></div>
            <div id="login-re"></div>
            <div id="search-re"></div>
            <div class="logo-re">
                <a href="<?php echo $this->createUrl("site/index/lang/$this->lang") ?>">
                    <img src="<?php echo $this->assets ?>img/logo.png" title="Tony English" width="350px">
                </a>
            </div>
        </div>
        <div class="row header">
            <div class="col">
                <div class="top">
                    <!-- menu top-->
                    <div class="menutop fl" id="replace-menu">
                        <ul>
                            <li class="<?= ($controller == 'site' && $action == 'index') ? 'active' : '' ?>" >
                                <a  href="<?php echo $this->createUrl("site/index/lang/$this->lang") ?>"><?php echo Yii::t('main', 'Home') ?></a>
                            </li>
                            <li class="<?= ($controller == 'site' && $action == 'courses') ? 'active' : '' ?>">
                                <a href="<?php echo $this->createUrl("site/courses/lang/$this->lang") ?>"><?php echo Yii::t('main', 'Courses') ?></a>
                            </li>
                            <li class="<?= ($controller == 'news' && $action == 'index') ? 'active' : '' ?>">
                                <a href="<?php echo $this->createUrl("news/index/lang/$this->lang") ?>"><?php echo Yii::t('main', 'News') ?></a>
                            </li>

                            <li class="<?= ($controller == 'library' && $action == 'index') ? 'active' : '' ?>">
                                <a href="<?php echo $this->createUrl("library/index/lang/$this->lang") ?>"><?php echo Yii::t('main', 'Library') ?></a>
                            </li>

                            <li class="<?= ($controller == 'site' && $action == 'about') ? 'active' : '' ?>">
                                <a href="<?php echo $this->createUrl("site/about/lang/$this->lang") ?>"><?php echo Yii::t('main', 'About us') ?></a>
                            </li>
                            <?php if (isset($this->userModel) && !empty($this->userModel)): ?>     
                                <li class="<?= ($controller == 'user' && $action == 'lecture') ? 'active' : '' ?>">
                                    <a href="<?php echo $this->createUrl("user/lecture/lang/$this->lang") ?>"><?php echo Yii::t('main', 'Lectures') ?></a>
                                </li>
                                <li class="<?= ($controller == 'user' && $action == 'message') ? 'active' : '' ?>">
                                    <a href="<?php echo $this->createUrl("user/message/lang/$this->lang") ?>"><?php echo Yii::t('main', 'Message') ?>
                                        <?php
                                        if (isset($this->userModel)):
                                            $curent_mail = $this->userModel->user_email;
                                            $newMess = Message::model()->findAllByAttributes(array('message_to' => $curent_mail, 'message_readed' => 0, 'delete_to' => 0, 'message_save' => 0));
                                        endif;
                                        ?>
                                        <?php
                                        if (isset($newMess)):
                                            if (count($newMess) > 0):
                                                ?>           
                                                <sup><span class="span-user"><?php echo count($newMess); ?></span></sup>
                                                <?php
                                            endif;
                                        endif;
                                        ?>   
                                    </a>
                                </li>
                            <?php endif; ?>
                                <li class="iconlang-re" id="iconlang-re"></li>

                        </ul>
                    </div>
                    <!-- end menu top-->
                    <!--lang -->
                    <!--<div class="span3 flrg">      
                        <div class="span5 flrg">
                    -->
                    <div class="flag-user flrg" id="replace-login">
                        <div class="icon-lang flrg" id="replace-icon-lang">                                
                            <?php if ($this->lang == 'en'): ?>
                                <a id="blackvi" href="<?php echo $this->createUrl("/vi") ?>">
                                   
                                </a>
                            <?php else : ?>
                                <a id="langen"  href="<?php echo $this->createUrl("/en") ?>">
                                    
                                </a>
                            <?php endif; ?>
                        </div>
                        <?php if (isset($this->userModel) && !empty($this->userModel)): ?>
                            <div class="inforuser fl">
                                <div class="imguser fl">
                                    <?php
                                    $userModel = $this->userModel;
                                    $avatar = $userModel->user_avatar;
                                    $legth = strlen($avatar);

                                    $fullname = $this->userModel->user_fullname;
                                    $arrName = explode(" ", $fullname);
                                    $i = count($arrName);
                                    $firstname = $arrName[$i - 1];
                                    if ($legth > 13):
                                        ?>
                                        <a href="<?php echo $this->createUrl("user/profile/lang/$this->lang") ?>">
                                            <img  class="avatar" src="<?php echo Yii::app()->baseUrl . "/" . $userModel->user_avatar ?>">
                                        </a>   
                                    <?php endif; ?>
                                    <?php if ($legth <= 13): ?>
                                        <a href="<?php echo $this->createUrl("user/profile/lang/$this->lang") ?>">
                                            <img class="avatar" src="<?php echo Yii::app()->baseUrl . "/uploads/user/no-avatar.jpg" ?>"><br/> 
                                        </a>
                                    <?php endif; ?>
                                </div>
                                <div class="nameuser fl">
                                    <a href="<?php echo $this->createUrl("user/profile/lang/$this->lang") ?>"><?php echo $firstname; ?></a>

                                </div>
                                <div class="clr"></div>
                                <!--                                <div class="sub-infor">
                                                                    <div class="icon-sub"></div>
                                                                    <div class="clr"></div>
                                                                    <div class="sub-infor-menu">
                                                                        <ul>
                                
                                <?php if (!isset($this->userModel) || empty($this->userModel)): ?>
                                                    
                                                                                                                                    <li>
                                                                                                                                        <a  id="login" href="<?php echo $this->createUrl("user/login/lang/$this->lang") ?>"><?php echo Yii::t('main', 'Login') ?></a>
                                                                                                                                    </li>
                                <?php else: ?>
                                                    
                                                                                                    <li>
                                                                                                        <a href="<?php echo $this->createUrl("user/logout/lang/$this->lang") ?>"><?php echo Yii::t('main', 'Logout') ?></a>
                                                                                                    </li>
                                <?php endif; ?> 
                                                                            <li>
                                                                                <a href="<?php echo $this->createUrl("user/logout/lang/$this->lang") ?>"><?php echo Yii::t('main', 'Information') ?></a>
                                                                            </li>
                                                                        </ul>
                                                                    </div>
                                                                </div>-->

                            </div>
                        <?php else: ?>

                            <a  id="login" href="<?php echo $this->createUrl("user/login/lang/$this->lang") ?>"><?php echo Yii::t('main', 'Login') ?></a>

                        <?php endif; ?> 
                    </div>
                    <!-- end user - flag -->

                    <!--
                                            </div>
                                        </div>
                    -->
                </div>
            </div>
        </div>
        <div class="clr"></div>
        <!--end top header-->
        <!-- logo - box search -->
        <div class="row<?= ($controller == 'site' && $action == 'index') ? ' logo-boxsearch ' : ' logo-boxsearch2' ?>">
            <div class="col">
                <div class="logo logo-main span3 fl">
                    <a href="<?php echo $this->createUrl("site/index/lang/$this->lang") ?>">
                        <img src="<?php echo $this->assets ?>img/logo.png" title="Tony English" width="350px">
                    </a>
                </div>
                <!-- box search-->
                <div class="padding-box-search span3 flrg" id="replace-search">
                    <div class="box-search flrg inputSearch" style="display: none">
                        <gcse:search></gcse:search>
                        <button class="icondown logo sear"></button>
                        <button class="iconsearch logo sear"></button>
                        <div class="clr"></div>
                        <ul class="searchOption" id="web" style="display: none">                 
                            <a href="javascript:;" onclick="websiteSearch($(this))" id="parentWeb"><li class="activeSearch"><img  id ="website" src="<?php echo $this->assets ?>img/icon/true_icon.gif"><?php echo Yii::t('main', 'Search the web') ?></li></a>       
                            <a href="javascript:;" onclick="dictionEV($(this))" id="parentDic"> <li class="unactiveSearch"> <img id="diction" style="display:none" src="<?php echo $this->assets ?>img/icon/true_icon.gif"><?php echo Yii::t('main', 'Dictionary') ?></li></a>     
                            <a href="https://translate.google.com.vn/?hl=en&tab=wT#en/vi/" onclick="return popupGoogle('https://translate.google.com.vn/?hl=en&tab=wT#en/vi/')"  > <li class="popupGoogle"><?php echo Yii::t('main', 'Translate the sentences') ?></li></a>     
                        </ul>
                    </div>
                    <div class="box-search flrg inputDiction" >
                        <script type='text/javascript'>var tudien_d = '1,2,3,4,5,6,7,9,8';
                            var tudien_fontsize = '15';
                            var tudien_inputsize = '15';
                            var tudien_bordercolor = 'b7d6e9';
                        </script>
                        <script type='text/javascript' src='<?php echo $this->assets ?>/js/tudien.js'></script>
                        <!--<button class="iconsearch logo"></button>-->
                        <button class="icondown logo dic"></button>
                        <button class="iconsearch logo dic"></button>
                        <div class="clr"></div>
                        <ul class="searchOption" id="dicsear" style="display: none">                 
                            <a href="javascript:;" onclick="websiteSearch($(this))" id="parentWeb"><li class="unactiveSearch"><img style="display: none" id ="website" src="<?php echo $this->assets ?>img/icon/true_icon.gif"><?php echo Yii::t('main', 'Search the web') ?></li></a>       
                            <a href="javascript:;" onclick="dictionEV($(this))" id="parentDic"> <li class="activeSearch"> <img id="diction"  src="<?php echo $this->assets ?>img/icon/true_icon.gif"><?php echo Yii::t('main', 'Dictionary') ?></li></a>     
                            <a href="https://translate.google.com.vn/?hl=en&tab=wT#en/vi/" onclick="return popupGoogle('https://translate.google.com.vn/?hl=en&tab=wT#en/vi/')"  > <li class="popupGoogle"><?php echo Yii::t('main', 'Translate the sentences') ?></li></a>     
                        </ul>
                    </div>
                    <div class="clr"></div>
                    <div class="icon-sub"></div>    
                    <div class="clr"></div>
                    <ul class="searchOption" style="display: none">                 
                        <a href="javascript:;" onclick="websiteSearch($(this))" id="parentWeb"><li class="activeSearch"><img  id ="website" src="<?php echo $this->assets ?>img/icon/true_icon.gif"><?php echo Yii::t('main', 'Search the web') ?></li></a>       
                        <a href="javascript:;" onclick="dictionEV($(this))" id="parentDic"> <li class="unactiveSearch"> <img id="diction" style="display:none" src="<?php echo $this->assets ?>img/icon/true_icon.gif"><?php echo Yii::t('main', 'Dictionary') ?></li></a>     
                        <a href="https://translate.google.com.vn/?hl=en&tab=wT#en/vi/" onclick="return popupGoogle('https://translate.google.com.vn/?hl=en&tab=wT#en/vi/')"  > <li class="popupGoogle"><?php echo Yii::t('main', 'Translate the sentences') ?></li></a>     
                    </ul>
                </div>
            </div>
        </div>
        <!-- end logo - boxsearch-->
        <div class="clr"></div>
        <!--<div>-->

        <div class="<?= ($controller == 'site' && $action == 'index') ? 'row' : 'col' ?>">
            <?php if ($controller != 'user'): ?>
                <?php echo $content; ?>
            <?php endif; ?>   
        </div>
        <?php if ($controller == 'user') : ?> 
            <!--user-->
            <!--            <div class=" row menuuser">
                            <ul>
                                <a href="<?php echo $this->createUrl("user/lecture/lang/$this->lang") ?>">
                                    <li style="border-right: 1px solid #ccc;" class="<?= ($controller == 'user' && $action == 'lecture') ? 'active' : '' ?>">
            <?php echo Yii::t('main', 'Lecture & Exercise') ?>
                                    </li>
                                </a>
                                <a href="<?php echo $this->createUrl("user/message/lang/$this->lang") ?>">
                                    <li style="border-right: 1px solid #ccc;" class="<?= ($controller == 'user' && $action == 'message') ? 'active' : '' ?>">
            <?php echo Yii::t('main', 'Message') ?> 
                                        <span class="span-user">
            <?php
            if (isset($this->userModel)):
                $curent_mail = $userModel->user_email;
                $newMess = Message::model()->findAllByAttributes(array('message_to' => $curent_mail, 'message_readed' => 0, 'delete_to' => 0, 'message_save' => 0));
                echo " " . count($newMess) . " ";
            endif;
            ?>
                                        </span>
            
                                    </li>
                                </a>
                                <a href="<?php echo $this->createUrl("user/library/lang/$this->lang") ?>">
                                    <li style="border-right: 1px solid #ccc;" class="<?= ($controller == 'user' && $action == 'library' || $action == 'exercise' ) ? 'active' : '' ?>">
            <?php echo Yii::t('main', 'Library') ?>
                                    </li>
                                </a>
                                <a href="<?php echo $this->createUrl("user/profile/lang/$this->lang") ?>">
                                    <li class="<?= ($controller == 'user' && $action == 'profile') ? 'active' : '' ?>">
            <?php echo Yii::t('main', 'Profile') ?>
                                    </li>
                                </a>
                            </ul>
                        </div> -->
            <?php echo $content; ?>
        <?php endif ?>                
        <div class="clr"></div>
        <div class="row footer">
            <div class="footertop">
                <div class="col">
                    <div class="firstmenu row fl">

                        <div class="m1 row fl">
                            <ul>
                                <li class="<?= ($controller == 'site' && $action == 'index') ? 'active' : '' ?>">
                                    <a href="<?php echo $this->createUrl("site/index/lang/$this->lang") ?>"><?php echo Yii::t('main', 'Home') ?></a>
                                </li>
                                <li class="<?= ($controller == 'site' && $action == 'courses') ? 'active' : '' ?>">
                                    <a href="<?php echo $this->createUrl("site/courses/lang/$this->lang") ?>"><?php echo Yii::t('main', 'Courses') ?></a>
                                </li>                                
                                <li class="<?= ($controller == 'news' && $action == 'index') ? 'active' : '' ?>">
                                    <a href="<?php echo $this->createUrl("news/index/lang/$this->lang") ?>"><?php echo Yii::t('main', 'News') ?></a>
                                </li>
                                <li class="<?= ($controller == 'library' && $action == 'index') ? 'active' : '' ?>">
                                    <a href="<?php echo $this->createUrl("library/index/lang/$this->lang") ?>"><?php echo Yii::t('main', 'Library') ?></a>
                                </li>
                                <li class="<?= ($controller == 'site' && $action == 'about') ? 'active' : '' ?>">
                                    <a href="<?php echo $this->createUrl("site/about/lang/$this->lang") ?>"><?php echo Yii::t('main', 'About us') ?></a>
                                </li>
                                <li class="<?= ($controller == 'site' && $action == 'contact') ? 'active' : '' ?>">
                                    <a href="<?php echo $this->createUrl("site/contact/lang/$this->lang") ?>"><?php echo Yii::t('main', 'Contact') ?></a>
                                </li>
                                <?php if (isset($this->userModel) && !empty($this->userModel)): ?>     
                                    <li class="<?= ($controller == 'user' && $action == 'lecture') ? 'active' : '' ?>">
                                        <a href="<?php echo $this->createUrl("user/lecture/lang/$this->lang") ?>"><?php echo Yii::t('main', 'Lectures') ?></a>
                                    </li>
                                    <li class="<?= ($controller == 'user' && $action == 'message') ? 'active' : '' ?>">
                                        <a href="<?php echo $this->createUrl("user/message/lang/$this->lang") ?>"><?php echo Yii::t('main', 'Message') ?>
                                            <?php
                                            if (isset($this->userModel)):
                                                $curent_mail = $userModel->user_email;
                                                $newMess = Message::model()->findAllByAttributes(array('message_to' => $curent_mail, 'message_readed' => 0, 'delete_to' => 0, 'message_save' => 0));
                                            endif;
                                            ?>
                                            <?php
                                            if (isset($newMess)):
                                                if (count($newMess) > 0):
                                                    ?>           
                                                    <sup><span class="span-user"><?php echo count($newMess); ?></span></sup>
                                                    <?php
                                                endif;
                                            endif;
                                            ?>   
                                        </a>
                                    </li>
                                <?php endif; ?>
                            </ul>
                        </div>

                    </div>
                </div>   
            </div>
            <div class="clr"></div>
            <div class="footerinfor-re"></div>
            <div class="footerinfor">
                <div class="col">
                    <div class="finforl fl">
                        <div class="conf">

                            <p>
                                <?php echo Yii::t('main', 'Address') ?>: <?= (isset($arr_webconfig['company_address']) && trim($arr_webconfig['company_address']) != '') ? $arr_webconfig['company_address'] : '' ?><br/>

                                <?php echo Yii::t('main', 'Contact') ?>:  <?= (isset($arr_webconfig['company_tel']) && trim($arr_webconfig['company_tel']) != '') ? $arr_webconfig['company_tel'] : '' ?><br/>

                                <?php echo Yii::t('main', 'Email') ?>:  <?= (isset($arr_webconfig['company_email']) && trim($arr_webconfig['company_email']) != '') ? $arr_webconfig['company_email'] : '' ?><br/>
                            </p>
                        </div>
                    </div>
                    <div class="finforr fl">
                        <p><?php echo Yii::t('main', 'Our terms and other documents below changed in Aug 2012. Please familiarise yourself with the new ones') ?></p>
                        <ul>
                            <li>
                                <a href="<?php echo $this->createUrl("site/sitemap/lang/$this->lang") ?>"><?php echo Yii::t('main', "Site map") ?></a>
                            </li>
                            <li>|</li>
                            <li>
                                <?php
                                    $c_about = AboutCategory::model()->findByAttributes(array('deleted' => 0, 'ac_status' => 1, 'ac_type' => 1));

                                    $about = About::model()->findAllByAttributes(array('deleted' => 0, 'about_status' => 1, 'ac_id' => $c_about->ac_id));
                                    if (isset($about) && !empty($about)) {
                                        if ($this->lang == "vi") {
                                            $url = $about[0]->about_title_url_vi;
                                        }else {
                                            $url = $about[0]->about_title_url_en;
                                        }
                                    }else{$url = '';}
                                ?>
                                <a href="<?php echo $this->createUrl("site/contact/lang/$this->lang/name/$url") ?>"><?php echo Yii::t('main', 'Terms & conditions') ?></a>
                            </li>
                            <li>|</li>
                            <li>
                                <p> @2013 TONYENGLISH</p>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <!--</div>-->
        <div class="top_page" id="top_page" title="Back to top" >abc</div>

        <form name="frm" id ="frmLec" method="POST" action="<?php echo $this->createUrl("user/lecture/lang/$this->lang") ?>"><input type="text" name ="cl" style="display: none"value="<?php echo $this->cc_id ?>"></form>       
        <script type="text/javascript" src="<?php echo $this->assets ?>/js/jquery.stepslide.js"></script>
        <script>
//            $("#blackvi").hover(function(){
//                $("#redvi").show();
//                $("#blackvi").hide();
//            },function(){
//                $("#redvi").hide();
//                $("#blackvi").show();
//            })


//            $(".menutop ul li").click(function (){
//                $(".active").removeClass("active");
//                $(this).addClass("active");
//            })
            $(".btn-search-re").click(function (){
                var abc ={'display':'block'};
                $("#replace-search").css(abc);
            })
            function popupGoogle(url) {
               newwindow = window.open(url,'name','height=400,width=550');
                    if (window.focus) {newwindow.focus()}
                        return false;
                }
                
//            function popupGoogle(){
//                    window.open("",'width=700,height=500,toolbar=0,menubar=0,location=0,status=1,scrollbars=1,resizable=1,left=0,top=0')
//            }
            function websiteSearch(e) {
                $("#diction").hide();
                $("#website").show();
//                $(e).css("font-weight","bold");

                $("#parentDic li").addClass("unactiveSearch");
                $("#parentDic li").removeClass("activeSearch");
                $("#parentWeb li").addClass("activeSearch");
                $("#parentWeb li").removeClass("unactiveSearch");

                $(".inputDiction").hide();
                $(".inputSearch").show();
            }
            function dictionEV(e) {
                $("#diction").show();
                $("#website").hide();

                $("#parentDic li").addClass("activeSearch");
                $("#parentDic li").removeClass("unactiveSearch");
                $("#parentWeb li").addClass("unactiveSearch");
                $("#parentWeb li").removeClass("activeSearch");

                $(".inputDiction").show();
                $(".inputSearch").hide();
//                $(e).css("font-weight","bold");
            }
//            $(".tudienblurred").show();
            $("input").focus(function() {
                $(".searchOption").hide();
            })
            $(".sear").click(function() {
                $("#web").show();

            })
            $(".dic").click(function() {
                $("#dicsear").show();

            })
//                            $("#1tudienInput").focus(function() {
//                                $(".searchOption").hide();
//                            })
            $(".padding-box-search").hover(function() {
                $(".searchOption").hide();
            })
            $('.inforuser').click(function() {
                window.location.assign("<?php echo $this->createUrl("user/profile/lang/$this->lang") ?>")
            })
            $(".totop").click(function() {
                $('html, body').animate({scrollTop: $("#header").offset().top - 200}, 100);
            })

            function hide_otherstep(first, hide, show)
            {
                last = first + num_el;
                i = 0;
                $('.stepslide > ul li').each(function() {
                    if (i < first || i > last)
                        $(this).hide(hide);
                    else
                        $(this).show(show);
                    i++;
                });
            }
        </script>
        <script>
            $("#lec").click(function() {
                $("#frmLec").submit();
            })

            $('.carousel').carousel();
            $("#age").datepick({
                yearRange: "-50:-6",
                showOn: "button",
                buttonImage: "<?php echo $this->assets ?>img/calendar.gif",
                buttonImageOnly: true,
                dateFormat: "MM d','yyyy"
            })
            //  $( "#age" ).datepick();
            //$('#age').datepick(
            //"option", "dateFormat", "MM d','yyyy");                    

            function showDate(date) {
                alert('The date chosen is ' + date);
            }
            function newmess() {
                $('a#newmess').click();
            }

            $(document).ready(function() {
                $('a#newmess').colorbox();
            });
//            $(document).ready(function(){    
//                $('a#contact').colorbox();
//            });
            function popuplogin() {
//                alert("kekekekke");
//                $('a#login').click();
            }
            $(document).ready(function() {
                $('a#login').colorbox();
            });
//             $(document).ready(function(){    
//                $('#member').colorbox();
//            });	
            $(document).ready(function() {
                $('#video').colorbox();
            });
            $(document).ready(function() {
                $(".more").colorbox();
            });
            function setup_tiny() {
                tinyMCE.init({
                    // General options
                    mode: "textareas",
                    //theme : "advanced",
                    entity_encoding: "raw",
                    editor_deselector: "mceNoEditor",
                    style_formats:
                            [
                                {title: 'List 1-a không căn lề', selector: 'ul', styles: {'marginLeft': '0'}},
                                {title: 'List 1-a lề cấp 1', selector: 'ul', styles: {'marginLeft': '30'}},
                                {title: 'List 1-a lề cấp 2', selector: 'ul', styles: {'marginLeft': '60'}},
                                {title: 'List biểu tượng không căn lề', selector: 'ol', styles: {'marginLeft': '0'}},
                                {title: 'List biểu tượng lề cấp 1', selector: 'ol', styles: {'marginLeft': '10'}},
                                {title: 'List biểu tượng lề cấp 2', selector: 'ol', styles: {'marginLeft': '20'}},
                            ],
                    plugins: "pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,wordcount,advlist,equation",
                    //
                    document_base_url: "http://tonyenglish.vn/",
                    relative_urls: false,
                    //Theme options
                    theme_advanced_buttons1: "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,styleselect,formatselect,fontselect,fontsizeselect",
                    theme_advanced_buttons2: "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,code,|,insertdate,inserttime,preview",
                    theme_advanced_buttons3: "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,",
                    //theme_advanced_buttons4 : "insertlayer,moveforward,movebackward,absolute,|,styleprops,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,nonbreaking,template,pagebreak,restoredraft",
                    theme_advanced_resizing: false,
                    force_p_newlines: false,
                    forced_root_block: '',
                    //            relative_urls : true,
                    document_base_url : "/<?php echo Yii::app()->baseUrl; ?>"
                });
            }
        </script>
        <!--    	<div id="loading">
                <div style="float:left; padding-top:3px;"><img src="<?php echo $this->assets; ?>img/loading1.gif" width="16" height="11" class="fl" /></div><div style="float:left; padding-left:8px;"><?= Yii::t('main', 'Loading') ?>...</div>
                <div class="clr"></div>
                </div>-->
        <a  style="display: none" href="<?= $this->createUrl("user/newmess/lang/$this->lang") ?>" id="newmess"></a>
    </body>
</html>
