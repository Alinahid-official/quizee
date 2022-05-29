<!doctype html>
<html class="no-js" lang="en">

<head>
  <!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-180348448-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-180348448-1');
</script>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Online Quiz System</title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">


    <link rel="stylesheet" href="css1/bootstrap.min.css">
    <script src="https://kit.fontawesome.com/8f045748b8.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="css1/style.css">
    <link rel="stylesheet" href="css1/font-awesome.min.css">
    <link rel="icon" href="images/favicon.png" type="image/gif">
</head>
<body>
<div class="all-content-wrapper">

    <div class="header-advance-area">
        <div class="header-top-area">
            <div class="container-fluid">
                <div class="row" style="background-color:black">
                    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                        <div class="header-top-wraper">
                            <div class="row">
                                <div class="col-lg-1 col-md-0 col-sm-1 col-xs-12"style="background-color:black;">
                                    <!-- <div class="menu-switcher-pro">
                                        <button type="button" id="sidebarCollapse" class="btn bar-button-pro header-drl-controller-btn btn-info navbar-btn">
                                            <i class="educate-icon educate-nav"></i>
                                        </button>
                                    </div> -->
                                </div>
                                <div class="col-lg-6 col-md-7 col-sm-6 col-xs-12"style="background-color:black;">
                                    <div class="header-top-menu tabl-d-n">
                                        <ul class="nav navbar-nav mai-top-nav">
                                            <li class="nav-item"><a href="old_exam_results.php" class="nav-link"style="padding-bottom: 0px;">Last Results</a>
                                            </li>
                                            <li class="nav-item"><a href="logout.php" class="nav-link"style="padding-bottom: 0px;">Logout</a>
                                            </li>

                                        </ul>
                                    </div>
                                </div>
                                <div class="col-lg-5 col-md-5 col-sm-12 col-xs-12" style="background-color:black;">
                                    <div class="header-right-info">
                                        <ul class="nav navbar-nav mai-top-nav header-right-menu">


                                          <li class="nav-item">
                                              <a href="#" data-toggle="dropdown" role="button" aria-expanded="false" class="nav-link dropdown-toggle">
                                                  <img src="img/avatar-mini2.jpg" alt="" />
                                                  <span class="admin-name"><?php echo $_SESSION["username"]; ?></span>
                                                  <i class="fa fa-angle-down edu-icon edu-down-arrow"></i>
                                              </a>
                                              <ul role="menu" class="dropdown-header-top author-log dropdown-menu animated zoomIn">
                                                  <li><a href="logout.php"><span class="edu-icon edu-locked author-log-ic"></span>Log Out</a>
                                                  </li>
                                              </ul>
                                          </li>

                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Mobile Menu start -->

        <!-- Mobile Menu end -->
        <div class="breadcome-area">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12"style="background-color:#a6f6f1">
                        <div class="breadcome-list" style="margin-bottom: 0px;margin-top: 0px;background-color:#a6f6f1">
                            <div class="row">
                                <div class="col-lg-12 col-md-6 col-sm-6 col-xs-12 text-right">
                                    <ul class="breadcome-menu">
                                      <li style="color:red;"><strong>Time Remaining</strong></li>
                                        <li><div id="countdowntimer" style="font-weight: bold;color: red;display: block;"></div>
                                        </li>

                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
<script type="text/javascript">
    setInterval(function(){
        timer();
    },1000);
    function timer()
    {
        var xmlhttp=new XMLHttpRequest();
        xmlhttp.onreadystatechange=function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {

                if(xmlhttp.responseText=="00:00:01")
                {
                    window.location="result.php";
                }

                document.getElementById("countdowntimer").innerHTML=xmlhttp.responseText;

            }
        };
        xmlhttp.open("GET","forajax/load_timer.php",true);
        xmlhttp.send(null);
    }

    </script>
