# -*- coding: utf-8 -*-
# from urllib.parse import unquote, urlparse
from bs4 import BeautifulSoup
import re
import pandas as pd
import requests

def get_data(url,request_object):

	html_content = request_object.text 
	soup = BeautifulSoup(html_content, "lxml")

	questions = soup.select('.category-mcq-questions .entry-content > p')

	col_names = ["crawl_url", "title", "question", "option_1", "option_2", "option_3", "option_4", "option_5", "option_6", "correct_option", "Board", "Class", "Subject", "Chapter", "Topic", "Sub-topic"]
	result = "result.csv"

	pd.DataFrame(columns = col_names).to_csv(result, sep="\t", index=False, encoding='utf-8')

	for question in questions:
		data_dict = {}
		data_dict["crawl_url"] = url
		data_dict["title"] = soup.title.get_text()

		temp_question_list = question.get_text(separator=" ").split('\n')

		print(temp_question_list)
		data_dict["question"] = temp_question_list[1]

		for idx, option in enumerate(temp_question_list[2:]):
			option = re.sub(r"^\([a-z]\)", " ", option, flags = re.I)
			data_dict["option_"+str(idx+1)] = option

		if question.find_next("details"):
			if question.find_next("details").find("p"):
				data_dict["correct_option"] = question.find_next("details").find("p").get_text()
				data_dict["correct_option"] = re.sub(r"^answer\s*:", " ", data_dict["correct_option"], flags = re.I)


		print(data_dict)
		print("*"*5)

		for temp in data_dict.keys():
			if type(data_dict[temp])==str:
				data_dict[temp] = re.sub(r"\s+", " ", data_dict[temp])
				data_dict[temp] = data_dict[temp].strip()

		pd.DataFrame([data_dict], columns = col_names).to_csv(result, sep="\t", index=False, header=False, encoding='utf-8', mode='a')



# url = "https://www.ncertbooks.guru/major-domains-of-the-earth-class-6-mcqs-questions-with-answers/"
url = "https://www.ncertbooks.guru/keeping-quiet-class-12-mcq-questions-with-answers/"

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
request_object = requests.get(url, headers=headers)


if(str(request_object.status_code).startswith("2")):   #for status check 200 series
	get_data(url,request_object)
	print("Done")
else:
	print("No Response from website")



"""
# h2 ~ ul > li > a[href*="mcq-questions"], h2 ~ ol > li > a[href*="mcq-questions"]

output from selector == Yes than go deep with BFS
else add url in csv and crawl


queue_list > addition of all selector links with domain match
visited_list

"""




# html_content = """ 

# <!DOCTYPE html>
# <html lang="en-US">
# <head>
# 	<meta charset="UTF-8">
# 	<link rel="profile" href="https://gmpg.org/xfn/11">
# 	<meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />

# 	<!-- This site is optimized with the Yoast SEO Premium plugin v16.8 (Yoast SEO v16.8) - https://yoast.com/wordpress/plugins/seo/ -->
# 	<title>The Earth in the Solar System Class 6 MCQs Questions with Answers</title>
# 	<meta name="description" content="The Earth in the Solar System Class 6 MCQs Questions with Answers" />
# 	<link rel="canonical" href="https://www.ncertbooks.guru/the-earth-in-the-solar-system-class-6-mcqs-questions-with-answers/" />
# 	<meta property="og:locale" content="en_US" />
# 	<meta property="og:type" content="article" />
# 	<meta property="og:title" content="The Earth in the Solar System Class 6 MCQs Questions with Answers" />
# 	<meta property="og:description" content="The Earth in the Solar System Class 6 MCQs Questions with Answers" />
# 	<meta property="og:url" content="https://www.ncertbooks.guru/the-earth-in-the-solar-system-class-6-mcqs-questions-with-answers/" />
# 	<meta property="og:site_name" content="NCERT Books" />
# 	<meta property="article:published_time" content="2020-12-15T08:04:43+00:00" />
# 	<meta name="twitter:card" content="summary_large_image" />
# 	<meta name="twitter:label1" content="Written by" />
# 	<meta name="twitter:data1" content="Kishen" />
# 	<meta name="twitter:label2" content="Est. reading time" />
# 	<meta name="twitter:data2" content="3 minutes" />
# 	<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://www.ncertbooks.guru/#organization","name":"GetMyUni","url":"https://www.ncertbooks.guru/","sameAs":[],"logo":{"@type":"ImageObject","@id":"https://www.ncertbooks.guru/#logo","inLanguage":"en-US","url":"https://www.ncertbooks.guru/wp-content/uploads/2019/04/GetMyUni-Logo.png","contentUrl":"https://www.ncertbooks.guru/wp-content/uploads/2019/04/GetMyUni-Logo.png","width":518,"height":169,"caption":"GetMyUni"},"image":{"@id":"https://www.ncertbooks.guru/#logo"}},{"@type":"WebSite","@id":"https://www.ncertbooks.guru/#website","url":"https://www.ncertbooks.guru/","name":"NCERT Books","description":"Download NCERT Books and Solutions PDF","publisher":{"@id":"https://www.ncertbooks.guru/#organization"},"potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://www.ncertbooks.guru/?s={search_term_string}"},"query-input":"required name=search_term_string"}],"inLanguage":"en-US"},{"@type":"WebPage","@id":"https://www.ncertbooks.guru/the-earth-in-the-solar-system-class-6-mcqs-questions-with-answers/#webpage","url":"https://www.ncertbooks.guru/the-earth-in-the-solar-system-class-6-mcqs-questions-with-answers/","name":"The Earth in the Solar System Class 6 MCQs Questions with Answers","isPartOf":{"@id":"https://www.ncertbooks.guru/#website"},"datePublished":"2020-12-15T08:04:43+00:00","dateModified":"2020-12-15T08:04:43+00:00","description":"The Earth in the Solar System Class 6 MCQs Questions with Answers","breadcrumb":{"@id":"https://www.ncertbooks.guru/the-earth-in-the-solar-system-class-6-mcqs-questions-with-answers/#breadcrumb"},"inLanguage":"en-US","potentialAction":[{"@type":"ReadAction","target":["https://www.ncertbooks.guru/the-earth-in-the-solar-system-class-6-mcqs-questions-with-answers/"]}]},{"@type":"BreadcrumbList","@id":"https://www.ncertbooks.guru/the-earth-in-the-solar-system-class-6-mcqs-questions-with-answers/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://www.ncertbooks.guru/"},{"@type":"ListItem","position":2,"name":"The Earth in the Solar System Class 6 MCQs Questions with Answers"}]},{"@type":"Article","@id":"https://www.ncertbooks.guru/the-earth-in-the-solar-system-class-6-mcqs-questions-with-answers/#article","isPartOf":{"@id":"https://www.ncertbooks.guru/the-earth-in-the-solar-system-class-6-mcqs-questions-with-answers/#webpage"},"author":{"@id":"https://www.ncertbooks.guru/#/schema/person/bbfca6b65b1a6fd05c80768dd027e4fb"},"headline":"The Earth in the Solar System Class 6 MCQs Questions with Answers","datePublished":"2020-12-15T08:04:43+00:00","dateModified":"2020-12-15T08:04:43+00:00","mainEntityOfPage":{"@id":"https://www.ncertbooks.guru/the-earth-in-the-solar-system-class-6-mcqs-questions-with-answers/#webpage"},"wordCount":657,"commentCount":0,"publisher":{"@id":"https://www.ncertbooks.guru/#organization"},"articleSection":["MCQ Questions"],"inLanguage":"en-US","potentialAction":[{"@type":"CommentAction","name":"Comment","target":["https://www.ncertbooks.guru/the-earth-in-the-solar-system-class-6-mcqs-questions-with-answers/#respond"]}]},{"@type":"Person","@id":"https://www.ncertbooks.guru/#/schema/person/bbfca6b65b1a6fd05c80768dd027e4fb","name":"Kishen","image":{"@type":"ImageObject","@id":"https://www.ncertbooks.guru/#personlogo","inLanguage":"en-US","url":"https://secure.gravatar.com/avatar/ec8ffca00d0f4ef593fb758376ff2a7d?s=96&d=wavatar&r=g","contentUrl":"https://secure.gravatar.com/avatar/ec8ffca00d0f4ef593fb758376ff2a7d?s=96&d=wavatar&r=g","caption":"Kishen"},"sameAs":["https://www.ncertbooks.guru/"],"url":"https://www.ncertbooks.guru/author/kishen/"}]}</script>
# 	<!-- / Yoast SEO Premium plugin. -->


# <link rel="amphtml" href="https://www.ncertbooks.guru/the-earth-in-the-solar-system-class-6-mcqs-questions-with-answers/amp/" /><meta name="generator" content="AMP for WP 1.0.77.6"/><link rel='dns-prefetch' href='//s.w.org' />
# <link rel="alternate" type="application/rss+xml" title="NCERT Books &raquo; Feed" href="https://www.ncertbooks.guru/feed/" />
# <link rel="alternate" type="application/rss+xml" title="NCERT Books &raquo; Comments Feed" href="https://www.ncertbooks.guru/comments/feed/" />
# <link rel="alternate" type="application/rss+xml" title="NCERT Books &raquo; The Earth in the Solar System Class 6 MCQs Questions with Answers Comments Feed" href="https://www.ncertbooks.guru/the-earth-in-the-solar-system-class-6-mcqs-questions-with-answers/feed/" />
# 		<script>
# 			window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/13.1.0\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/13.1.0\/svg\/","svgExt":".svg","source":{"concatemoji":"https:\/\/www.ncertbooks.guru\/wp-includes\/js\/wp-emoji-release.min.js?ver=5.8.2"}};
# 			!function(e,a,t){var n,r,o,i=a.createElement("canvas"),p=i.getContext&&i.getContext("2d");function s(e,t){var a=String.fromCharCode;p.clearRect(0,0,i.width,i.height),p.fillText(a.apply(this,e),0,0);e=i.toDataURL();return p.clearRect(0,0,i.width,i.height),p.fillText(a.apply(this,t),0,0),e===i.toDataURL()}function c(e){var t=a.createElement("script");t.src=e,t.defer=t.type="text/javascript",a.getElementsByTagName("head")[0].appendChild(t)}for(o=Array("flag","emoji"),t.supports={everything:!0,everythingExceptFlag:!0},r=0;r<o.length;r++)t.supports[o[r]]=function(e){if(!p||!p.fillText)return!1;switch(p.textBaseline="top",p.font="600 32px Arial",e){case"flag":return s([127987,65039,8205,9895,65039],[127987,65039,8203,9895,65039])?!1:!s([55356,56826,55356,56819],[55356,56826,8203,55356,56819])&&!s([55356,57332,56128,56423,56128,56418,56128,56421,56128,56430,56128,56423,56128,56447],[55356,57332,8203,56128,56423,8203,56128,56418,8203,56128,56421,8203,56128,56430,8203,56128,56423,8203,56128,56447]);case"emoji":return!s([10084,65039,8205,55357,56613],[10084,65039,8203,55357,56613])}return!1}(o[r]),t.supports.everything=t.supports.everything&&t.supports[o[r]],"flag"!==o[r]&&(t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&t.supports[o[r]]);t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&!t.supports.flag,t.DOMReady=!1,t.readyCallback=function(){t.DOMReady=!0},t.supports.everything||(n=function(){t.readyCallback()},a.addEventListener?(a.addEventListener("DOMContentLoaded",n,!1),e.addEventListener("load",n,!1)):(e.attachEvent("onload",n),a.attachEvent("onreadystatechange",function(){"complete"===a.readyState&&t.readyCallback()})),(n=t.source||{}).concatemoji?c(n.concatemoji):n.wpemoji&&n.twemoji&&(c(n.twemoji),c(n.wpemoji)))}(window,document,window._wpemojiSettings);
# 		</script>
# 		<style>
# img.wp-smiley,
# img.emoji {
# 	display: inline !important;
# 	border: none !important;
# 	box-shadow: none !important;
# 	height: 1em !important;
# 	width: 1em !important;
# 	margin: 0 .07em !important;
# 	vertical-align: -0.1em !important;
# 	background: none !important;
# 	padding: 0 !important;
# }
# </style>
# 	<link rel='stylesheet' id='wp-block-library-css'  href='https://www.ncertbooks.guru/wp-includes/css/dist/block-library/style.min.css?ver=5.8.2' media='all' />
# <link rel='stylesheet' id='generate-comments-css'  href='https://www.ncertbooks.guru/wp-content/themes/generatepress/assets/css/components/comments.min.css?ver=3.0.4' media='all' />
# <link rel='stylesheet' id='generate-widget-areas-css'  href='https://www.ncertbooks.guru/wp-content/themes/generatepress/assets/css/components/widget-areas.min.css?ver=3.0.4' media='all' />
# <link rel='stylesheet' id='generate-style-css'  href='https://www.ncertbooks.guru/wp-content/themes/generatepress/assets/css/main.min.css?ver=3.0.4' media='all' />
# <style id='generate-style-inline-css'>
# body{background-color:#f7f8f9;color:#222222;}a{color:#1e73be;}a:hover, a:focus, a:active{color:#000000;}.wp-block-group__inner-container{max-width:1200px;margin-left:auto;margin-right:auto;}body, button, input, select, textarea{font-family:-apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";}body{line-height:1.5;}.entry-content > [class*="wp-block-"]:not(:last-child){margin-bottom:1.5em;}.main-navigation .main-nav ul ul li a{font-size:14px;}.sidebar .widget, .footer-widgets .widget{font-size:17px;}@media (max-width:768px){h1{font-size:31px;}h2{font-size:27px;}h3{font-size:24px;}h4{font-size:22px;}h5{font-size:19px;}}.top-bar{background-color:#636363;color:#ffffff;}.top-bar a{color:#ffffff;}.top-bar a:hover{color:#303030;}.site-header{background-color:#ffffff;}.main-title a,.main-title a:hover{color:#803487;}.site-description{color:#757575;}.mobile-menu-control-wrapper .menu-toggle,.mobile-menu-control-wrapper .menu-toggle:hover,.mobile-menu-control-wrapper .menu-toggle:focus,.has-inline-mobile-toggle #site-navigation.toggled{background-color:rgba(0, 0, 0, 0.02);}.main-navigation,.main-navigation ul ul{background-color:#ffffff;}.main-navigation .main-nav ul li a,.menu-toggle, .main-navigation .menu-bar-items{color:#515151;}.main-navigation .main-nav ul li:hover > a,.main-navigation .main-nav ul li:focus > a, .main-navigation .main-nav ul li.sfHover > a, .main-navigation .menu-bar-item:hover > a, .main-navigation .menu-bar-item.sfHover > a{color:#7a8896;background-color:#ffffff;}button.menu-toggle:hover,button.menu-toggle:focus{color:#515151;}.main-navigation .main-nav ul li[class*="current-menu-"] > a{color:#7a8896;background-color:#ffffff;}.main-navigation .main-nav ul li[class*="current-menu-"] > a:hover,.main-navigation .main-nav ul li[class*="current-menu-"].sfHover > a{color:#7a8896;background-color:#ffffff;}.navigation-search input[type="search"],.navigation-search input[type="search"]:active, .navigation-search input[type="search"]:focus, .main-navigation .main-nav ul li.search-item.active > a, .main-navigation .menu-bar-items .search-item.active > a{color:#7a8896;background-color:#ffffff;}.main-navigation ul ul{background-color:#eaeaea;}.main-navigation .main-nav ul ul li a{color:#515151;}.main-navigation .main-nav ul ul li:hover > a,.main-navigation .main-nav ul ul li:focus > a,.main-navigation .main-nav ul ul li.sfHover > a{color:#7a8896;background-color:#eaeaea;}.main-navigation .main-nav ul ul li[class*="current-menu-"] > a{color:#7a8896;background-color:#eaeaea;}.main-navigation .main-nav ul ul li[class*="current-menu-"] > a:hover,.main-navigation .main-nav ul ul li[class*="current-menu-"].sfHover > a{color:#7a8896;background-color:#eaeaea;}.separate-containers .inside-article, .separate-containers .comments-area, .separate-containers .page-header, .one-container .container, .separate-containers .paging-navigation, .inside-page-header{background-color:#ffffff;}.entry-title a{color:#222222;}.entry-title a:hover{color:#55555e;}.entry-meta{color:#595959;}.sidebar .widget{background-color:#ffffff;}.footer-widgets{color:#ffffff;background-color:#803487;}.footer-widgets a{color:#ffffff;}.footer-widgets .widget-title{color:#ffffff;}.site-info{color:#ffffff;background-color:#803487;}.site-info a{color:#ffffff;}.site-info a:hover{color:#d3d3d3;}.footer-bar .widget_nav_menu .current-menu-item a{color:#d3d3d3;}input[type="text"],input[type="email"],input[type="url"],input[type="password"],input[type="search"],input[type="tel"],input[type="number"],textarea,select{color:#666666;background-color:#fafafa;border-color:#cccccc;}input[type="text"]:focus,input[type="email"]:focus,input[type="url"]:focus,input[type="password"]:focus,input[type="search"]:focus,input[type="tel"]:focus,input[type="number"]:focus,textarea:focus,select:focus{color:#666666;background-color:#ffffff;border-color:#bfbfbf;}button,html input[type="button"],input[type="reset"],input[type="submit"],a.button,a.wp-block-button__link:not(.has-background){color:#ffffff;background-color:#55555e;}button:hover,html input[type="button"]:hover,input[type="reset"]:hover,input[type="submit"]:hover,a.button:hover,button:focus,html input[type="button"]:focus,input[type="reset"]:focus,input[type="submit"]:focus,a.button:focus,a.wp-block-button__link:not(.has-background):active,a.wp-block-button__link:not(.has-background):focus,a.wp-block-button__link:not(.has-background):hover{color:#ffffff;background-color:#3f4047;}a.generate-back-to-top{background-color:rgba( 0,0,0,0.4 );color:#ffffff;}a.generate-back-to-top:hover,a.generate-back-to-top:focus{background-color:rgba( 0,0,0,0.6 );color:#ffffff;}@media (max-width: 768px){.main-navigation .menu-bar-item:hover > a, .main-navigation .menu-bar-item.sfHover > a{background:none;color:#515151;}}.nav-below-header .main-navigation .inside-navigation.grid-container, .nav-above-header .main-navigation .inside-navigation.grid-container{padding:0px 20px 0px 20px;}.site-main .wp-block-group__inner-container{padding:40px;}.separate-containers .paging-navigation{padding-top:20px;padding-bottom:20px;}.entry-content .alignwide, body:not(.no-sidebar) .entry-content .alignfull{margin-left:-40px;width:calc(100% + 80px);max-width:calc(100% + 80px);}.rtl .menu-item-has-children .dropdown-menu-toggle{padding-left:20px;}.rtl .main-navigation .main-nav ul li.menu-item-has-children > a{padding-right:20px;}@media (max-width:768px){.separate-containers .inside-article, .separate-containers .comments-area, .separate-containers .page-header, .separate-containers .paging-navigation, .one-container .site-content, .inside-page-header{padding:30px;}.site-main .wp-block-group__inner-container{padding:30px;}.inside-top-bar{padding-right:30px;padding-left:30px;}.inside-header{padding-right:30px;padding-left:30px;}.widget-area .widget{padding-top:30px;padding-right:30px;padding-bottom:30px;padding-left:30px;}.footer-widgets-container{padding-top:30px;padding-right:30px;padding-bottom:30px;padding-left:30px;}.inside-site-info{padding-right:30px;padding-left:30px;}.entry-content .alignwide, body:not(.no-sidebar) .entry-content .alignfull{margin-left:-30px;width:calc(100% + 60px);max-width:calc(100% + 60px);}.one-container .site-main .paging-navigation{margin-bottom:20px;}}/* End cached CSS */.is-right-sidebar{width:30%;}.is-left-sidebar{width:30%;}.site-content .content-area{width:70%;}@media (max-width: 768px){.main-navigation .menu-toggle,.sidebar-nav-mobile:not(#sticky-placeholder){display:block;}.main-navigation ul,.gen-sidebar-nav,.main-navigation:not(.slideout-navigation):not(.toggled) .main-nav > ul,.has-inline-mobile-toggle #site-navigation .inside-navigation > *:not(.navigation-search):not(.main-nav){display:none;}.nav-align-right .inside-navigation,.nav-align-center .inside-navigation{justify-content:space-between;}.has-inline-mobile-toggle .mobile-menu-control-wrapper{display:flex;flex-wrap:wrap;}.has-inline-mobile-toggle .inside-header{flex-direction:row;text-align:left;flex-wrap:wrap;}.has-inline-mobile-toggle .header-widget,.has-inline-mobile-toggle #site-navigation{flex-basis:100%;}.nav-float-left .has-inline-mobile-toggle #site-navigation{order:10;}}
# </style>
# <link rel="https://api.w.org/" href="https://www.ncertbooks.guru/wp-json/" /><link rel="alternate" type="application/json" href="https://www.ncertbooks.guru/wp-json/wp/v2/posts/31024" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://www.ncertbooks.guru/xmlrpc.php?rsd" />
# <link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://www.ncertbooks.guru/wp-includes/wlwmanifest.xml" /> 
# <meta name="generator" content="WordPress 5.8.2" />
# <link rel='shortlink' href='https://www.ncertbooks.guru/?p=31024' />
# <link rel="alternate" type="application/json+oembed" href="https://www.ncertbooks.guru/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.ncertbooks.guru%2Fthe-earth-in-the-solar-system-class-6-mcqs-questions-with-answers%2F" />
# <link rel="alternate" type="text/xml+oembed" href="https://www.ncertbooks.guru/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fwww.ncertbooks.guru%2Fthe-earth-in-the-solar-system-class-6-mcqs-questions-with-answers%2F&#038;format=xml" />
# <script  id="feedify_webscript" >
# var feedify = feedify || {};
# window.feedify_options={fedify_url:"https://feedify.net/"};
# (function (window, document){
# 	function addScript( script_url ){
# 		var s = document.createElement('script');
# 		s.type = 'text/javascript';
# 		s.src = script_url;
# 		document.getElementsByTagName('head')[0].appendChild(s);
# 	}
# 	addScript('https://tpcf.feedify.net/uploads/settings/e786d5702cdee916125fce646ead8442.js?ts='+Math.random());
# 	addScript('https://cdn.feedify.net/getjs/feedbackembad.min.js');
# })(window, document);
# </script>
# <link rel="manifest" href="/manifest.json">
# <!-- Global site tag (gtag.js) - Google Analytics -->
# <script async src="https://www.googletagmanager.com/gtag/js?id=UA-129294821-1"></script>
# <script>
#   window.dataLayer = window.dataLayer || [];
#   function gtag(){dataLayer.push(arguments);}
#   gtag('js', new Date());

#   gtag('config', 'UA-129294821-1');
# </script>

# <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9285780544011795"
#      crossorigin="anonymous"></script>

# <script async>(function(s,u,m,o,j,v){j=u.createElement(m);v=u.getElementsByTagName(m)[0];j.async=1;j.src=o;j.dataset.sumoSiteId='25ee81e7df6162858063ec65a2499feccbc72891df07b955c464739333697656';v.parentNode.insertBefore(j,v)})(window,document,'script','//load.sumo.com/');</script><link rel="pingback" href="https://www.ncertbooks.guru/xmlrpc.php">
# <meta name="viewport" content="width=device-width, initial-scale=1"></head>

# <body class="post-template-default single single-post postid-31024 single-format-standard wp-embed-responsive post-image-above-header post-image-aligned-center sticky-menu-fade right-sidebar nav-float-right separate-containers header-aligned-left dropdown-hover" itemtype="https://schema.org/Blog" itemscope>
# 	<a class="screen-reader-text skip-link" href="#content" title="Skip to content">Skip to content</a>		<header id="masthead" class="site-header has-inline-mobile-toggle" itemtype="https://schema.org/WPHeader" itemscope>
# 			<div class="inside-header grid-container">
# 				<div class="site-branding">
# 						<p class="main-title" itemprop="headline">
# 					<a href="https://www.ncertbooks.guru/" rel="home">
# 						NCERT Books
# 					</a>
# 				</p>
						
# 					</div>	<nav id="mobile-menu-control-wrapper" class="main-navigation mobile-menu-control-wrapper">
# 				<button class="menu-toggle" aria-controls="primary-menu" aria-expanded="false" data-nav="site-navigation">
# 			<span class="gp-icon icon-menu-bars"><svg viewBox="0 0 512 512" aria-hidden="true" role="img" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1em" height="1em">
# 						<path d="M0 96c0-13.255 10.745-24 24-24h464c13.255 0 24 10.745 24 24s-10.745 24-24 24H24c-13.255 0-24-10.745-24-24zm0 160c0-13.255 10.745-24 24-24h464c13.255 0 24 10.745 24 24s-10.745 24-24 24H24c-13.255 0-24-10.745-24-24zm0 160c0-13.255 10.745-24 24-24h464c13.255 0 24 10.745 24 24s-10.745 24-24 24H24c-13.255 0-24-10.745-24-24z" />
# 					</svg><svg viewBox="0 0 512 512" aria-hidden="true" role="img" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1em" height="1em">
# 						<path d="M71.029 71.029c9.373-9.372 24.569-9.372 33.942 0L256 222.059l151.029-151.03c9.373-9.372 24.569-9.372 33.942 0 9.372 9.373 9.372 24.569 0 33.942L289.941 256l151.03 151.029c9.372 9.373 9.372 24.569 0 33.942-9.373 9.372-24.569 9.372-33.942 0L256 289.941l-151.029 151.03c-9.373 9.372-24.569 9.372-33.942 0-9.372-9.373-9.372-24.569 0-33.942L222.059 256 71.029 104.971c-9.372-9.373-9.372-24.569 0-33.942z" />
# 					</svg></span><span class="screen-reader-text">Menu</span>		</button>
# 	</nav>
# 			<nav id="site-navigation" class="main-navigation sub-menu-right" itemtype="https://schema.org/SiteNavigationElement" itemscope>
# 			<div class="inside-navigation grid-container">
# 								<button class="menu-toggle" aria-controls="primary-menu" aria-expanded="false">
# 					<span class="gp-icon icon-menu-bars"><svg viewBox="0 0 512 512" aria-hidden="true" role="img" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1em" height="1em">
# 						<path d="M0 96c0-13.255 10.745-24 24-24h464c13.255 0 24 10.745 24 24s-10.745 24-24 24H24c-13.255 0-24-10.745-24-24zm0 160c0-13.255 10.745-24 24-24h464c13.255 0 24 10.745 24 24s-10.745 24-24 24H24c-13.255 0-24-10.745-24-24zm0 160c0-13.255 10.745-24 24-24h464c13.255 0 24 10.745 24 24s-10.745 24-24 24H24c-13.255 0-24-10.745-24-24z" />
# 					</svg><svg viewBox="0 0 512 512" aria-hidden="true" role="img" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1em" height="1em">
# 						<path d="M71.029 71.029c9.373-9.372 24.569-9.372 33.942 0L256 222.059l151.029-151.03c9.373-9.372 24.569-9.372 33.942 0 9.372 9.373 9.372 24.569 0 33.942L289.941 256l151.03 151.029c9.372 9.373 9.372 24.569 0 33.942-9.373 9.372-24.569 9.372-33.942 0L256 289.941l-151.029 151.03c-9.373 9.372-24.569 9.372-33.942 0-9.372-9.373-9.372-24.569 0-33.942L222.059 256 71.029 104.971c-9.372-9.373-9.372-24.569 0-33.942z" />
# 					</svg></span><span class="screen-reader-text">Menu</span>				</button>
# 				<div id="primary-menu" class="main-nav"><ul id="menu-botom-menu" class=" menu sf-menu"><li id="menu-item-9126" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-9126"><a href="https://www.ncertbooks.guru/ncert-books-pdf/">NCERT Books<span role="presentation" class="dropdown-menu-toggle"><span class="gp-icon icon-arrow"><svg viewBox="0 0 330 512" aria-hidden="true" role="img" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1em" height="1em">
# 						<path d="M305.913 197.085c0 2.266-1.133 4.815-2.833 6.514L171.087 335.593c-1.7 1.7-4.249 2.832-6.515 2.832s-4.815-1.133-6.515-2.832L26.064 203.599c-1.7-1.7-2.832-4.248-2.832-6.514s1.132-4.816 2.832-6.515l14.162-14.163c1.7-1.699 3.966-2.832 6.515-2.832 2.266 0 4.815 1.133 6.515 2.832l111.316 111.317 111.316-111.317c1.7-1.699 4.249-2.832 6.515-2.832s4.815 1.133 6.515 2.832l14.162 14.163c1.7 1.7 2.833 4.249 2.833 6.515z" fill-rule="nonzero"/>
# 					</svg></span></span></a>
# <ul class="sub-menu">
# 	<li id="menu-item-9536" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9536"><a href="https://www.ncertbooks.guru/ncert-books-for-class-1/">NCERT Books for Class 1</a></li>
# 	<li id="menu-item-9537" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9537"><a href="https://www.ncertbooks.guru/ncert-books-for-class-2/">NCERT Books for Class 2</a></li>
# 	<li id="menu-item-9538" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9538"><a href="https://www.ncertbooks.guru/ncert-books-for-class-3/">NCERT Books for Class 3</a></li>
# 	<li id="menu-item-9539" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9539"><a href="https://www.ncertbooks.guru/ncert-books-for-class-4/">NCERT Books for Class 4</a></li>
# 	<li id="menu-item-9540" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9540"><a href="https://www.ncertbooks.guru/ncert-books-for-class-5/">NCERT Books for Class 5</a></li>
# 	<li id="menu-item-9541" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9541"><a href="https://www.ncertbooks.guru/ncert-books-for-class-6/">NCERT Books for Class 6</a></li>
# 	<li id="menu-item-9542" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9542"><a href="https://www.ncertbooks.guru/ncert-books-class-7/">NCERT Books for Class 7</a></li>
# 	<li id="menu-item-9543" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9543"><a href="https://www.ncertbooks.guru/ncert-books-for-class-8/">NCERT Books for Class 8</a></li>
# 	<li id="menu-item-9544" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9544"><a href="https://www.ncertbooks.guru/ncert-books-class-9/">NCERT Books for Class 9</a></li>
# 	<li id="menu-item-9545" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9545"><a href="https://www.ncertbooks.guru/ncert-books-for-class-10/">NCERT Books for Class 10</a></li>
# 	<li id="menu-item-9546" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9546"><a href="https://www.ncertbooks.guru/ncert-books-for-class-11/">NCERT Books for Class 11</a></li>
# 	<li id="menu-item-9547" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9547"><a href="https://www.ncertbooks.guru/ncert-books-for-class-12/">NCERT Books for Class 12</a></li>
# </ul>
# </li>
# <li id="menu-item-9552" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-9552"><a href="https://www.ncertbooks.guru/cbse-ncert-solutions-pdf/">NCERT Solutions<span role="presentation" class="dropdown-menu-toggle"><span class="gp-icon icon-arrow"><svg viewBox="0 0 330 512" aria-hidden="true" role="img" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1em" height="1em">
# 						<path d="M305.913 197.085c0 2.266-1.133 4.815-2.833 6.514L171.087 335.593c-1.7 1.7-4.249 2.832-6.515 2.832s-4.815-1.133-6.515-2.832L26.064 203.599c-1.7-1.7-2.832-4.248-2.832-6.514s1.132-4.816 2.832-6.515l14.162-14.163c1.7-1.699 3.966-2.832 6.515-2.832 2.266 0 4.815 1.133 6.515 2.832l111.316 111.317 111.316-111.317c1.7-1.699 4.249-2.832 6.515-2.832s4.815 1.133 6.515 2.832l14.162 14.163c1.7 1.7 2.833 4.249 2.833 6.515z" fill-rule="nonzero"/>
# 					</svg></span></span></a>
# <ul class="sub-menu">
# 	<li id="menu-item-9555" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9555"><a href="https://www.ncertbooks.guru/ncert-solutions-for-class-12-pdf/">NCERT Solutions for Class 12</a></li>
# 	<li id="menu-item-9556" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9556"><a href="https://www.ncertbooks.guru/ncert-solutions-for-class-11-pdf/">NCERT Solutions for Class 11</a></li>
# 	<li id="menu-item-9557" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9557"><a href="https://www.ncertbooks.guru/ncert-solutions-for-class-10-pdf/">NCERT Solutions for Class 10</a></li>
# 	<li id="menu-item-9558" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9558"><a href="https://www.ncertbooks.guru/ncert-solutions-for-class-9-pdf/">NCERT Solutions for Class 9</a></li>
# 	<li id="menu-item-9559" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9559"><a href="https://www.ncertbooks.guru/ncert-solutions-for-class-8-pdf/">NCERT Solutions for Class 8</a></li>
# 	<li id="menu-item-9560" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9560"><a href="https://www.ncertbooks.guru/ncert-solutions-for-class-7-pdf/">NCERT Solutions for Class 7</a></li>
# 	<li id="menu-item-9561" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9561"><a href="https://www.ncertbooks.guru/ncert-solutions-for-class-6-pdf/">NCERT Solutions for Class 6</a></li>
# 	<li id="menu-item-9562" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9562"><a href="https://www.ncertbooks.guru/ncert-solutions-class-5/">NCERT Solutions for Class 5</a></li>
# </ul>
# </li>
# <li id="menu-item-16473" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-16473"><a href="https://www.ncertbooks.guru/mcq-questions/">MCQ Questions<span role="presentation" class="dropdown-menu-toggle"><span class="gp-icon icon-arrow"><svg viewBox="0 0 330 512" aria-hidden="true" role="img" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1em" height="1em">
# 						<path d="M305.913 197.085c0 2.266-1.133 4.815-2.833 6.514L171.087 335.593c-1.7 1.7-4.249 2.832-6.515 2.832s-4.815-1.133-6.515-2.832L26.064 203.599c-1.7-1.7-2.832-4.248-2.832-6.514s1.132-4.816 2.832-6.515l14.162-14.163c1.7-1.699 3.966-2.832 6.515-2.832 2.266 0 4.815 1.133 6.515 2.832l111.316 111.317 111.316-111.317c1.7-1.699 4.249-2.832 6.515-2.832s4.815 1.133 6.515 2.832l14.162 14.163c1.7 1.7 2.833 4.249 2.833 6.515z" fill-rule="nonzero"/>
# 					</svg></span></span></a>
# <ul class="sub-menu">
# 	<li id="menu-item-39752" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-39752"><a href="https://mcqquestions.guru/">MCQ Questions</a></li>
# 	<li id="menu-item-38745" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-38745"><a href="https://www.ncertbooks.guru/mcq-questions/amp/#MCQ_Questions_for_Class_6_with_Answers">MCQ Questions for Class 6</a></li>
# 	<li id="menu-item-38746" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-38746"><a href="https://www.ncertbooks.guru/mcq-questions/amp/#MCQ_Questions_for_Class_7_with_Answers">MCQ Questions for Class 7</a></li>
# 	<li id="menu-item-38747" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-38747"><a href="https://www.ncertbooks.guru/mcq-questions/amp/#MCQ_Questions_for_Class_8_with_Answers">MCQ Questions for Class 8</a></li>
# 	<li id="menu-item-38748" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-38748"><a href="https://www.ncertbooks.guru/mcq-questions/amp/#MCQ_Questions_for_Class_9_with_Answers">MCQ Questions for Class 9</a></li>
# 	<li id="menu-item-38749" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-38749"><a href="https://www.ncertbooks.guru/mcq-questions/amp/#MCQ_Questions_for_Class_10_with_Answers">MCQ Questions for Class 10</a></li>
# 	<li id="menu-item-38750" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-38750"><a href="https://www.ncertbooks.guru/mcq-questions/amp/#MCQ_Questions_for_Class_11_with_Answers">MCQ Questions for Class 11</a></li>
# 	<li id="menu-item-38751" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-38751"><a href="https://www.ncertbooks.guru/mcq-questions/amp/#MCQ_Questions_for_Class_12_with_Answers">MCQ Questions for Class 12</a></li>
# </ul>
# </li>
# <li id="menu-item-9563" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-9563"><a href="https://www.ncertbooks.guru/cbse/">CBSE<span role="presentation" class="dropdown-menu-toggle"><span class="gp-icon icon-arrow"><svg viewBox="0 0 330 512" aria-hidden="true" role="img" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1em" height="1em">
# 						<path d="M305.913 197.085c0 2.266-1.133 4.815-2.833 6.514L171.087 335.593c-1.7 1.7-4.249 2.832-6.515 2.832s-4.815-1.133-6.515-2.832L26.064 203.599c-1.7-1.7-2.832-4.248-2.832-6.514s1.132-4.816 2.832-6.515l14.162-14.163c1.7-1.699 3.966-2.832 6.515-2.832 2.266 0 4.815 1.133 6.515 2.832l111.316 111.317 111.316-111.317c1.7-1.699 4.249-2.832 6.515-2.832s4.815 1.133 6.515 2.832l14.162 14.163c1.7 1.7 2.833 4.249 2.833 6.515z" fill-rule="nonzero"/>
# 					</svg></span></span></a>
# <ul class="sub-menu">
# 	<li id="menu-item-16474" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-16474"><a href="https://www.ncertbooks.guru/study-material/">Study Material</a></li>
# 	<li id="menu-item-9564" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9564"><a href="https://www.ncertbooks.guru/cbse-syllabus/">CBSE Syllabus</a></li>
# 	<li id="menu-item-9565" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9565"><a href="https://www.ncertbooks.guru/cbse-full-form/">CBSE Full Form</a></li>
# </ul>
# </li>
# <li id="menu-item-9572" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-9572"><a href="https://www.ncertbooks.guru/category/icse/">ICSE<span role="presentation" class="dropdown-menu-toggle"><span class="gp-icon icon-arrow"><svg viewBox="0 0 330 512" aria-hidden="true" role="img" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1em" height="1em">
# 						<path d="M305.913 197.085c0 2.266-1.133 4.815-2.833 6.514L171.087 335.593c-1.7 1.7-4.249 2.832-6.515 2.832s-4.815-1.133-6.515-2.832L26.064 203.599c-1.7-1.7-2.832-4.248-2.832-6.514s1.132-4.816 2.832-6.515l14.162-14.163c1.7-1.699 3.966-2.832 6.515-2.832 2.266 0 4.815 1.133 6.515 2.832l111.316 111.317 111.316-111.317c1.7-1.699 4.249-2.832 6.515-2.832s4.815 1.133 6.515 2.832l14.162 14.163c1.7 1.7 2.833 4.249 2.833 6.515z" fill-rule="nonzero"/>
# 					</svg></span></span></a>
# <ul class="sub-menu">
# 	<li id="menu-item-9573" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9573"><a href="https://www.ncertbooks.guru/icse-books/">ICSE Books</a></li>
# 	<li id="menu-item-36475" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-36475"><a href="https://icsesolutions.com/">ICSE Solutions</a></li>
# 	<li id="menu-item-9575" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9575"><a href="https://mlaggarwalsolutions.com/">ML Aggarwal Solutions</a></li>
# 	<li id="menu-item-9574" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9574"><a href="https://www.ncertbooks.guru/selina-publishers-icse-solutions-pdf/">Selina Solutions</a></li>
# </ul>
# </li>
# <li id="menu-item-9576" class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-9576"><a href="https://www.ncertbooks.guru/category/books/">Books<span role="presentation" class="dropdown-menu-toggle"><span class="gp-icon icon-arrow"><svg viewBox="0 0 330 512" aria-hidden="true" role="img" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1em" height="1em">
# 						<path d="M305.913 197.085c0 2.266-1.133 4.815-2.833 6.514L171.087 335.593c-1.7 1.7-4.249 2.832-6.515 2.832s-4.815-1.133-6.515-2.832L26.064 203.599c-1.7-1.7-2.832-4.248-2.832-6.514s1.132-4.816 2.832-6.515l14.162-14.163c1.7-1.699 3.966-2.832 6.515-2.832 2.266 0 4.815 1.133 6.515 2.832l111.316 111.317 111.316-111.317c1.7-1.699 4.249-2.832 6.515-2.832s4.815 1.133 6.515 2.832l14.162 14.163c1.7 1.7 2.833 4.249 2.833 6.515z" fill-rule="nonzero"/>
# 					</svg></span></span></a>
# <ul class="sub-menu">
# 	<li id="menu-item-13241" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-13241"><a href="https://www.ncertbooks.guru/school-books/">School Books</a></li>
# 	<li id="menu-item-39596" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-39596"><a href="https://www.ncertbooks.guru/ebalbharati-books/">ebalbharati books</a></li>
# 	<li id="menu-item-9581" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-9581"><a href="https://www.ncertbooks.guru/amazon-books/">Amazon Books</a></li>
# 	<li id="menu-item-36813" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-36813"><a href="https://www.ncertbooks.guru/gk-general-knowledge/">GK General Knowledge</a></li>
# </ul>
# </li>
# <li id="menu-item-17311" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-17311"><a href="https://www.ncertbooks.guru/course-details/">Course Details<span role="presentation" class="dropdown-menu-toggle"><span class="gp-icon icon-arrow"><svg viewBox="0 0 330 512" aria-hidden="true" role="img" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1em" height="1em">
# 						<path d="M305.913 197.085c0 2.266-1.133 4.815-2.833 6.514L171.087 335.593c-1.7 1.7-4.249 2.832-6.515 2.832s-4.815-1.133-6.515-2.832L26.064 203.599c-1.7-1.7-2.832-4.248-2.832-6.514s1.132-4.816 2.832-6.515l14.162-14.163c1.7-1.699 3.966-2.832 6.515-2.832 2.266 0 4.815 1.133 6.515 2.832l111.316 111.317 111.316-111.317c1.7-1.699 4.249-2.832 6.515-2.832s4.815 1.133 6.515 2.832l14.162 14.163c1.7 1.7 2.833 4.249 2.833 6.515z" fill-rule="nonzero"/>
# 					</svg></span></span></a>
# <ul class="sub-menu">
# 	<li id="menu-item-18796" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-18796"><a href="https://www.ncertbooks.guru/courses-after-10th/">Courses After 10th</a></li>
# 	<li id="menu-item-18799" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-18799"><a href="https://www.ncertbooks.guru/diploma-courses/">Diploma Courses</a></li>
# 	<li id="menu-item-18800" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-18800"><a href="https://www.ncertbooks.guru/computer-courses/">Computer Courses</a></li>
# 	<li id="menu-item-18797" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-18797"><a href="https://www.ncertbooks.guru/courses-after-12th/">Courses After 12th</a></li>
# 	<li id="menu-item-18798" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-18798"><a href="https://www.ncertbooks.guru/courses-after-mba/">Courses After MBA</a></li>
# 	<li id="menu-item-18801" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-18801"><a href="https://www.ncertbooks.guru/animation-courses/">Animation Courses</a></li>
# </ul>
# </li>
# </ul></div>			</div>
# 		</nav>
# 					</div>
# 		</header>
		
# 	<div id="page" class="site grid-container container hfeed">
# 				<div id="content" class="site-content">
			
# 	<div id="primary" class="content-area">
# 		<main id="main" class="site-main">
			
# <article id="post-31024" class="post-31024 post type-post status-publish format-standard hentry category-mcq-questions" itemtype="https://schema.org/CreativeWork" itemscope>
# 	<div class="inside-article">
# 					<header class="entry-header">
# 				<h1 class="entry-title" itemprop="headline">The Earth in the Solar System Class 6 MCQs Questions with Answers</h1>		<div class="entry-meta">
# 			<span class="posted-on"><time class="entry-date published" datetime="2020-12-15T13:34:43+05:30" itemprop="datePublished">December 15, 2020</time></span> <span class="byline">by <span class="author vcard" itemprop="author" itemtype="https://schema.org/Person" itemscope><a class="url fn n" href="https://www.ncertbooks.guru/author/kishen/" title="View all posts by Kishen" rel="author" itemprop="url"><span class="author-name" itemprop="name">Kishen</span></a></span></span> 		</div>
# 					</header>
			
# 		<div class="entry-content" itemprop="text">
# 			<p>Question 1.<br />
# How is the sky filled with after sunset and in the night?<br />
# (a) Bright objects<br />
# (b) Dim objects<br />
# (c) Both (a) and (b)<br />
# (d) None of these</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (c) Both (a) and (b)</p>
# </details>
# <hr />
# <p>Question 2.<br />
# What is the name given to the full moon night?<br />
# (a) Amavasya<br />
# (b) Poornima<br />
# (c) Both (a) and (b)<br />
# (d) None of these</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (b) Poornima</p>
# </details>
# <hr />
# <p>Question 3.<br />
# Which of the following name is given to the new moon?<br />
# (a) Poornima<br />
# (b) Amavasya<br />
# (c) Both (a) and ib)<br />
# (d) None of these</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (b) Amavasya</p>
# </details>
# <hr />
# <p>Question 4.<br />
# What are celestial bodies?<br />
# (a) The sun<br />
# (b) The moon<br />
# (c) All the shining bodies in the sky<br />
# (d) All of these</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (d) All of these</p>
# </details>
# <hr />
# <p>Question 5.<br />
# The celestial bodies which have their own heat and light are called<br />
# (a) planets<br />
# (b) stars<br />
# (c) satellites<br />
# (d) all of these</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (b) stars</p>
# </details>
# <hr />
# <p>Question 6.<br />
# Which is the most recognisable constellation?<br />
# (a) The saptarishi<br />
# (b) The moon<br />
# (c) The sun<br />
# (d) The mars</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (a) The saptarishi</p>
# </details>
# <hr />
# <p>Question 7.<br />
# The star which indicates the north is called<br />
# (a) pole star<br />
# (b) pole<br />
# (c) north pole<br />
# (d) south pole</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (a) pole star</p>
# </details>
# <hr />
# <p>Question 8.<br />
# The celestial bodies which do not have their own heat and light but are lit by the light of the stars are named as<br />
# (a) stars<br />
# (b) planets<br />
# (c) both (a) and (b)<br />
# (d) none of these</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (b) planets</p>
# </details>
# <hr />
# <p>Question 9.<br />
# The word ‘planet’ has been derived from the word ‘planetai’ which is named as<br />
# (a) Latin word<br />
# (b) German word<br />
# (c) Greek word<br />
# (d) English word</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (c) Greek word</p>
# </details>
# <hr />
# <p>Question 10.<br />
# Which celestial bodies form the solar system?<br />
# (a) The sun<br />
# (b) The planets<br />
# (c) The satellites, asteroids and meteoroids<br />
# (d) All of the above</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (d) All of the above</p>
# </details>
# <hr />
# <p>Question 11.<br />
# All the planets move around the sun in fixed elliptical path, these paths are called<br />
# (a) axis<br />
# (b) orbit<br />
# (e) both (a) and (b)<br />
# (d) none of these</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (b) orbit</p>
# </details>
# <hr />
# <p>Question 12.<br />
# Why is the shape of the earth geoid?<br />
# (a) It is slightly flattened at the poles<br />
# (b) It is spheroid at the poles<br />
# (c) Both (a) and (b)<br />
# (d) None of these</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (a) It is slightly flattened at the poles</p>
# </details>
# <hr />
# <p>Question 13.<br />
# The earth is called a unique planet due to<br />
# (a) neither too hot nor too cold<br />
# (b) presence of air and water<br />
# (c) oxygen, light supporting gas<br />
# (d) all of these</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (d) all of these</p>
# </details>
# <hr />
# <p>Question 14.<br />
# The earth is called a blue planet because of the presence of<br />
# (a) water<br />
# (b) blue colour<br />
# (c) brown colour<br />
# (d) red colour</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (a) water</p>
# </details>
# <hr />
# <p>Question 15.<br />
# Why do we see only one side of the moon from the earth?<br />
# (a) Because of moon moving around the earth in 27 days<br />
# (b) 27 days also taken in one spin<br />
# (c) Both (a) and (b)<br />
# (d) None of these</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (c) Both (a) and (b)</p>
# </details>
# <hr />
# <p>Question 16.<br />
# Why does the moon not have conditions favourable for life?<br />
# (a) because of non existent of water<br />
# (b) because of non existent of air<br />
# (c) both (a) and (b)<br />
# (d) none of these</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (c) both (a) and (b)</p>
# </details>
# <hr />
# <p>Question 17.<br />
# Apart from stars, planets and satellites, there are numerous bodies which also move around the sun, what are these called?<br />
# (a) Stars<br />
# (b) Asteroids<br />
# (c) Meteoroids<br />
# (d) Planets</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (c) Meteoroids</p>
# </details>
# <hr />
# <p>Question 18.<br />
# Asteroids are found between the orbits of Jupiter and<br />
# (a) Mars<br />
# (b) Earth<br />
# (c) Venus<br />
# (d) Neptune</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (a) Mars</p>
# </details>
# <hr />
# <p>Question 19.<br />
# Meteoroids are made up of<br />
# (a) dust<br />
# (b) pieces of rocks<br />
# (c) gases<br />
# (d) none of these</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (b) pieces of rocks</p>
# </details>
# <hr />
# <p>Question 20.<br />
# What is called a cluster of millions of stars, shining white in the starry sky?<br />
# (a) Stars<br />
# (b) Planets<br />
# (c) Milky Way galaxy<br />
# (d) Satellites</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (c) Milky Way galaxy</p>
# </details>
# <hr />
# <p>Question 21.<br />
# What makes the universe?<br />
# (a) Millions of galaxies<br />
# (b) Millions of stars<br />
# (c) Earth<br />
# (d) Satellites</p>
# <details>
# <summary><span style="color: #0000ff;">Answer</span></summary>
# <p>Answer: (a) Millions of galaxies</p>
# </details>
# <hr />
# 		</div>

# 			</div>
# </article>

# 			<div class="comments-area">
# 				<div id="comments">

# 		<div id="respond" class="comment-respond">
# 		<h3 id="reply-title" class="comment-reply-title">Leave a Comment <small><a rel="nofollow" id="cancel-comment-reply-link" href="/the-earth-in-the-solar-system-class-6-mcqs-questions-with-answers/#respond" style="display:none;">Cancel reply</a></small></h3><p class="must-log-in">You must be <a href="https://www.ncertbooks.guru/wp-login.php?redirect_to=https%3A%2F%2Fwww.ncertbooks.guru%2Fthe-earth-in-the-solar-system-class-6-mcqs-questions-with-answers%2F">logged in</a> to post a comment.</p>	</div><!-- #respond -->
	
# </div><!-- #comments -->
# 			</div>

# 					</main>
# 	</div>

# 	<div id="right-sidebar" class="widget-area sidebar is-right-sidebar" itemtype="https://schema.org/WPSideBar" itemscope>
# 	<div class="inside-right-sidebar">
# 		<aside id="search-2" class="widget inner-padding widget_search"><form method="get" class="search-form" action="https://www.ncertbooks.guru/">
# 	<label>
# 		<span class="screen-reader-text">Search for:</span>
# 		<input type="search" class="search-field" placeholder="Search &hellip;" value="" name="s" title="Search for:">
# 	</label>
# 	<button class="search-submit" aria-label="Search"><span class="gp-icon icon-search"><svg viewBox="0 0 512 512" aria-hidden="true" role="img" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1em" height="1em">
# 						<path fill-rule="evenodd" clip-rule="evenodd" d="M208 48c-88.366 0-160 71.634-160 160s71.634 160 160 160 160-71.634 160-160S296.366 48 208 48zM0 208C0 93.125 93.125 0 208 0s208 93.125 208 208c0 48.741-16.765 93.566-44.843 129.024l133.826 134.018c9.366 9.379 9.355 24.575-.025 33.941-9.379 9.366-24.575 9.355-33.941-.025L337.238 370.987C301.747 399.167 256.839 416 208 416 93.125 416 0 322.875 0 208z"/>
# 					</svg></span></button></form>
# </aside><aside id="custom_html-3" class="widget_text widget inner-padding widget_custom_html"><div class="textwidget custom-html-widget"><ul>
# 			<li><a href="https://www.ncertbooks.guru/history-mcq-questions-quiz/" title="History MCQ Questions">History MCQ Questions</a></li>
# 			<li><a href="https://www.ncertbooks.guru/geography-mcq-quiz/" title="Geography MCQ Questions">Geography MCQ Questions</a></li>
# 				<li><a href="https://www.ncertbooks.guru/mcq-questions-on-computer-fundamentals/" title="MCQ Questions on Computer">MCQ Questions on Computer</a></li>
# 		<li><a href="https://www.ncertbooks.guru/maths-formulas/" title="Maths Formulas">Maths Formulas</a></li>
# <li><a href="https://www.ncertbooks.guru/physics-formulas/" title="Physics Formulas">Physics Formulas</a></li>
# <li><a href="https://www.ncertbooks.guru/chemistry-formulas/" title="Chemistry Formulas">Chemistry Formulas</a></li>
# 	<li><a href="https://www.ncertbooks.guru/ncert-books-class-12-maths/" title="NCERT Books for Class 12 Maths">NCERT Books for Class 12 Maths</a></li>
# <li><a href="https://www.ncertbooks.guru/ncert-books-class-11-maths/" title="NCERT Books for Class 11 Maths">NCERT Books for Class 11 Maths</a></li>
# <li><a href="https://www.ncertbooks.guru/ncert-books-class-10-maths/" title="NCERT Books for Class 10 Maths">NCERT Books for Class 10 Maths</a></li>
# <li><a href="https://www.ncertbooks.guru/ncert-books-class-9-maths/" title="NCERT Books for Class 9 Maths">NCERT Books for Class 9 Maths</a></li>
# <li><a href="https://www.ncertbooks.guru/ncert-books-class-8-maths/" title="NCERT Books for Class 8 Maths">NCERT Books for Class 8 Maths</a></li>
# <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
# <!-- guru_ads -->
# <ins class="adsbygoogle"
#      style="display:block"
#      data-ad-client="ca-pub-9285780544011795"
#      data-ad-slot="5323492646"
#      data-ad-format="auto"
#      data-full-width-responsive="true"></ins>
# <script>
# (adsbygoogle = window.adsbygoogle || []).push({});
# </script>
# <li><a href="https://www.ncertbooks.guru/ncert-books-class-7-maths/" title="NCERT Books for Class 7 Maths">NCERT Books for Class 7 Maths</a></li>
# <li><a href="https://www.ncertbooks.guru/ncert-books-class-6-maths/" title="NCERT Books for Class 6 Maths">NCERT Books for Class 6 Maths</a></li>
# 	<li><a href="https://www.ncertbooks.guru/ncert-solutions-for-class-10-maths-pdf/" title="NCERT Solutions for Class 10 Maths">NCERT Solutions for Class 10 Maths</a></li>
# 	<li><a href="https://www.ncertbooks.guru/neet-biology-mcq/" title="NEET Biology MCQ Questions">NEET Biology MCQ Questions</a></li>
# <li><a href="https://www.ncertbooks.guru/neet-physics-mcq/" title="NEET Physics MCQ Questions">NEET Physics MCQ Questions</a></li>
# 	<li><a href="https://www.ncertbooks.guru/neet-chemistry-mcq/" title="NEET Chemistry MCQ Questions">NEET Chemistry MCQ Questions</a></li>
# </ul>
# </div></aside>
# 		<aside id="recent-posts-2" class="widget inner-padding widget_recent_entries">
# 		<h2 class="widget-title">Recent Posts</h2>
# 		<ul>
# 											<li>
# 					<a href="https://www.ncertbooks.guru/self-concept-essay/">Self Concept Essay | Positive and Negative Self Concept, Long and Short Essays on Self Concept Theory</a>
# 									</li>
# 											<li>
# 					<a href="https://www.ncertbooks.guru/obesity-essay/">Obesity Essay | Causes, Effects, Disadvantages, How to Cure Obesity?</a>
# 									</li>
# 											<li>
# 					<a href="https://www.ncertbooks.guru/how-to-become-a-loco-pilot-in-india/">How To Become A Loco Pilot In India | Types, Duties, Selection Procedure, Eligibility Criteria and Salary</a>
# 									</li>
# 											<li>
# 					<a href="https://www.ncertbooks.guru/how-to-become-a-machine-learning-engineer-in-india/">How To Become A Machine Learning Engineer In India | Role, Skills Required, Eligibility Criteria, Job Oppurtunities, Scope and Salary</a>
# 									</li>
# 											<li>
# 					<a href="https://www.ncertbooks.guru/how-to-become-a-makeup-artist-in-india/">How To Become A Makeup Artist In India | Skills Required, Eligibility Criteria, Salary, Industries and Steps</a>
# 									</li>
# 											<li>
# 					<a href="https://www.ncertbooks.guru/how-to-become-a-marine-biologist-in-india/">How To Become A Marine Biologist In India | Career Path, Skillset, Education Qualification</a>
# 									</li>
# 											<li>
# 					<a href="https://www.ncertbooks.guru/how-to-become-a-mathematician-in-india/">How To Become A Mathematician In India | Career and Job Opportunities for Mathematicians</a>
# 									</li>
# 											<li>
# 					<a href="https://www.ncertbooks.guru/how-to-become-a-marine-engineer-in-india/">How To Become A Marine Engineer In India | Career Path, Eligibility Criteria and Top Colleges</a>
# 									</li>
# 											<li>
# 					<a href="https://www.ncertbooks.guru/how-to-become-a-district-magistrate-in-india/">How to Become a District Magistrate in India | Eligibility Criteria, Skillset, Career Path and Salary</a>
# 									</li>
# 											<li>
# 					<a href="https://www.ncertbooks.guru/how-to-become-a-mutual-fund-agent-in-india/">How To Become A Mutual Fund Agent In India | How do Mutual Funds Agents earn their income?</a>
# 									</li>
# 					</ul>

# 		</aside><aside id="media_video-2" class="widget inner-padding widget_media_video"><h2 class="widget-title">NCERT की बुक्स अब ऑनलाइन कर सकते हैं Download, बस ये स्टेप्स करें Follow</h2><div style="width:100%;" class="wp-video"><!--[if lt IE 9]><script>document.createElement('video');</script><![endif]-->
# <video class="wp-video-shortcode" id="video-31024-1" preload="metadata" controls="controls"><source type="video/youtube" src="https://www.youtube.com/watch?v=nd-0HFd58P8&#038;_=1" /><a href="https://www.youtube.com/watch?v=nd-0HFd58P8">https://www.youtube.com/watch?v=nd-0HFd58P8</a></video></div></aside>	</div>
# </div>

# 	</div>
# </div>


# <div class="site-footer">
# 				<div id="footer-widgets" class="site footer-widgets">
# 				<div class="footer-widgets-container grid-container">
# 					<div class="inside-footer-widgets">
# 							<div class="footer-widget-1">
# 		<aside id="block-3" class="widget inner-padding widget_block">
# <ul><li><span style="color:#ffc846" class="has-inline-color"><strong>Free Textbook Solutions</strong></span></li><li><a rel="noreferrer noopener" href="https://www.ncertbooks.guru/cbse-ncert-solutions-pdf/" target="_blank">NCERT Solutions</a></li><li><a href="https://www.ncertbooks.guru/ncert-solutions-class-5/">NCERT Solutions for Class 5</a></li><li><a rel="noreferrer noopener" href="https://www.ncertbooks.guru/ncert-solutions-for-class-6-pdf/" target="_blank">NCERT Solutions for Class 6</a></li><li><a rel="noreferrer noopener" href="https://www.ncertbooks.guru/ncert-solutions-for-class-7-pdf/" target="_blank">NCERT Solutions for Class 7</a></li><li><a rel="noreferrer noopener" href="https://www.ncertbooks.guru/ncert-solutions-for-class-8-pdf/" target="_blank">NCERT Solutions for Class 8</a></li><li><a rel="noreferrer noopener" href="https://www.ncertbooks.guru/ncert-solutions-for-class-9-pdf/" target="_blank">NCERT Solutions for Class 9</a></li><li><a rel="noreferrer noopener" href="https://www.ncertbooks.guru/ncert-solutions-for-class-10-pdf/" target="_blank">NCERT Solutions for Class 10</a></li><li><a rel="noreferrer noopener" href="https://www.ncertbooks.guru/ncert-solutions-for-class-11-pdf/" target="_blank">NCERT Solutions for Class 11</a></li><li><a rel="noreferrer noopener" href="https://www.ncertbooks.guru/ncert-solutions-for-class-12-pdf/" target="_blank">NCERT Solutions for Class 12</a></li><li><a rel="noreferrer noopener" href="https://www.ncertbooks.guru/rd-sharma-solutions-pdf/" target="_blank">RD Sharma Solutions</a></li><li><a rel="noreferrer noopener" href="https://www.ncertbooks.guru/rs-aggarwal-solutions-pdf/" target="_blank">RS Aggarwal Solutions</a></li><li><a href="https://www.ncertbooks.guru/selina-publishers-icse-solutions-pdf/">Selina ICSE Solutions</a></li><li><a rel="noreferrer noopener" href="https://www.ncertbooks.guru/ml-aggarwal-solutions/" target="_blank">ML Aggarwal Solutions</a></li><li><a href="https://www.ncertbooks.guru/ts-grewal-solutions-pdf/">TS Grewal Solutions</a></li><li><a href="https://www.ncertbooks.guru/hc-verma-solutions-download/">HC Verma Solutions</a></li><li><a href="https://www.ncertbooks.guru/kc-sinha-solutions/">KC Sinha Solutions</a></li><li><a href="https://www.ncertbooks.guru/maths-formulas/">Maths Formulas</a></li><li><a rel="noreferrer noopener" href="https://www.ncertbooks.guru/physics-formulas/" target="_blank">Physics Formulas</a></li><li><a rel="noreferrer noopener" href="https://www.ncertbooks.guru/chemistry-formulas/" target="_blank">Chemistry Formulas</a></li><li></li></ul>
# </aside>	</div>
# 		<div class="footer-widget-2">
# 		<aside id="block-4" class="widget inner-padding widget_block">
# <ul><li><span style="color:#ffc846" class="has-inline-color"><strong>Important Books</strong></span></li><li><a rel="noreferrer noopener" href="https://www.ncertbooks.guru/ncert-books-pdf/" target="_blank">NCERT Books</a></li><li><a rel="noreferrer noopener" href="https://www.ncertbooks.guru/ncert-hindi-books/" target="_blank">NCERT Hindi Books</a></li><li><a href="https://www.ncertbooks.guru/ncert-exemplar-books/">NCERT Exemplar Books</a></li><li><a href="https://www.ncertbooks.guru/old-ncert-books/">Old NCERT Books</a></li><li><a href="https://www.ncertbooks.guru/upsc-books/">UPSC Books</a></li><li><a href="https://www.ncertbooks.guru/icse-books/">ICSE Books</a></li><li><a href="https://www.ncertbooks.guru/nios-books/">NIOS Books</a></li><li><a href="https://www.ncertbooks.guru/python-books/">Python Books</a></li><li><a href="https://www.ncertbooks.guru/b-tech-books/">B.Tech Books</a></li><li><a href="https://www.ncertbooks.guru/m-tech-books/">M.Tech Books</a></li><li><a style="font-size: inherit;" href="https://www.ncertbooks.guru/ph-d-books/">Ph.D. Books</a></li><li><a href="https://www.ncertbooks.guru/b-com-books/">B.Com Books</a></li><li><a href="https://www.ncertbooks.guru/m-com-books/">M.Com Books</a></li><li><a href="https://www.ncertbooks.guru/b-ed-books/">B.Ed Books</a></li><li><a href="https://www.ncertbooks.guru/m-sc-books/">M.Sc Books</a></li><li><a href="https://www.ncertbooks.guru/bca-books/"><span style="font-size: inherit;">BCA Books</span></a></li><li><a href="https://www.ncertbooks.guru/mca-books/">MCA Books</a></li><li><a href="https://www.ncertbooks.guru/rrb-ntpc-books/">RRB NTPC Books</a></li><li><a href="https://www.ncertbooks.guru/rrb-alp-books/">RRB ALP Books</a></li><li><a href="https://www.ncertbooks.guru/rrb-sse-books/">RRB SSE Books</a></li><li><a href="https://www.ncertbooks.guru/telugu-academy-books/amp/">Telugu Academy Books</a></li><li></li><li></li></ul>
# </aside>	</div>
# 		<div class="footer-widget-3">
# 		<aside id="block-10" class="widget inner-padding widget_block">
# <ul><li><span style="color:#ffc846" class="has-inline-color"><strong>State Board Textbooks</strong></span></li><li><a href="https://www.ncertbooks.guru/scert-kerala-textbooks/">SCERT Kerala Textbooks</a></li><li><a href="https://www.ncertbooks.guru/maharashtra-state-board-books/">Maharashtra State Board Books</a></li><li><a href="https://www.ncertbooks.guru/ts-scert-books/">TS SCERT Books</a></li><li><a href="https://www.ncertbooks.guru/samacheer-kalvi-books/">Samacheer Kalvi Books</a></li><li><a href="https://www.ncertbooks.guru/up-board-books-pdf/">UP Board Books</a></li><li><a href="https://www.ncertbooks.guru/ap-scert-books/">AP SCERT Books</a></li><li><a href="https://www.ncertbooks.guru/bihar-state-board-books/">Bihar State Board Books</a></li><li><a href="https://www.ncertbooks.guru/chandigarh-school-books/">Chandigarh School Books</a></li><li><a href="https://www.ncertbooks.guru/chattisgarh-board-textbooks/">Chhattisgarh Board Textbooks</a></li><li><a href="https://www.ncertbooks.guru/gseb-textbooks/">GSEB Textbooks</a></li><li><a href="https://www.ncertbooks.guru/karnataka-state-board-books/">Karnataka State Board Books</a></li><li><a style="font-size: inherit;" href="https://www.ncertbooks.guru/mp-board-books/">MP Board Books</a></li><li><a style="font-size: inherit;" href="https://www.ncertbooks.guru/manipur-board-textbooks/">Manipur Board Textbooks</a></li><li><a href="https://www.ncertbooks.guru/mp-board-books/"></a><a href="https://www.ncertbooks.guru/meghalaya-board-books/">Meghalaya Board Books</a></li><li><a href="https://www.ncertbooks.guru/mp-board-books/"></a><a href="https://www.ncertbooks.guru/mizoram-board-textbooks/">Mizoram Board Textbooks</a></li><li><a href="https://www.ncertbooks.guru/mp-board-books/"></a><a href="https://www.ncertbooks.guru/bse-odisha-board-textbooks/">BSE Odisha Board Textbooks</a></li><li><a href="https://www.ncertbooks.guru/mp-board-books/"></a><a href="https://www.ncertbooks.guru/pseb-books/">PSEB Books</a></li><li><a href="https://www.ncertbooks.guru/mp-board-books/"></a><a href="https://www.ncertbooks.guru/rbse-books-pdf/">RBSE Books</a></li><li><a style="font-size: inherit;" href="https://www.ncertbooks.guru/tripura-board-books/">Tripura Board Books</a></li><li><a style="font-size: inherit;" href="https://www.ncertbooks.guru/west-bengal-board-books/">West Bengal Board Books</a></li></ul>
# </aside>	</div>
# 						</div>
# 				</div>
# 			</div>
# 					<footer class="site-info" itemtype="https://schema.org/WPFooter" itemscope>
# 			<div class="inside-site-info grid-container">
# 								<div class="copyright-bar">
# 					Copyright &copy; 2021 <a href="https://www.ncertbooks.guru/">NCERT Books</a>				</div>
# 			</div>
# 		</footer>
# 		</div>

# <link rel='stylesheet' id='mediaelement-css'  href='https://www.ncertbooks.guru/wp-includes/js/mediaelement/mediaelementplayer-legacy.min.css?ver=4.2.16' media='all' />
# <link rel='stylesheet' id='wp-mediaelement-css'  href='https://www.ncertbooks.guru/wp-includes/js/mediaelement/wp-mediaelement.min.css?ver=5.8.2' media='all' />
# <!--[if lte IE 11]>
# <script src='https://www.ncertbooks.guru/wp-content/themes/generatepress/assets/js/classList.min.js?ver=3.0.4' id='generate-classlist-js'></script>
# <![endif]-->
# <script id='generate-main-js-extra'>
# var generatepressMenu = {"toggleOpenedSubMenus":"1","openSubMenuLabel":"Open Sub-Menu","closeSubMenuLabel":"Close Sub-Menu"};
# </script>
# <script src='https://www.ncertbooks.guru/wp-content/themes/generatepress/assets/js/main.min.js?ver=3.0.4' id='generate-main-js'></script>
# <script src='https://www.ncertbooks.guru/wp-includes/js/comment-reply.min.js?ver=5.8.2' id='comment-reply-js'></script>
# <script src='https://www.ncertbooks.guru/wp-includes/js/wp-embed.min.js?ver=5.8.2' id='wp-embed-js'></script>
# <script src='https://www.ncertbooks.guru/wp-includes/js/jquery/jquery.min.js?ver=3.6.0' id='jquery-core-js'></script>
# <script src='https://www.ncertbooks.guru/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.3.2' id='jquery-migrate-js'></script>
# <script id='mediaelement-core-js-before'>
# var mejsL10n = {"language":"en","strings":{"mejs.download-file":"Download File","mejs.install-flash":"You are using a browser that does not have Flash player enabled or installed. Please turn on your Flash player plugin or download the latest version from https:\/\/get.adobe.com\/flashplayer\/","mejs.fullscreen":"Fullscreen","mejs.play":"Play","mejs.pause":"Pause","mejs.time-slider":"Time Slider","mejs.time-help-text":"Use Left\/Right Arrow keys to advance one second, Up\/Down arrows to advance ten seconds.","mejs.live-broadcast":"Live Broadcast","mejs.volume-help-text":"Use Up\/Down Arrow keys to increase or decrease volume.","mejs.unmute":"Unmute","mejs.mute":"Mute","mejs.volume-slider":"Volume Slider","mejs.video-player":"Video Player","mejs.audio-player":"Audio Player","mejs.captions-subtitles":"Captions\/Subtitles","mejs.captions-chapters":"Chapters","mejs.none":"None","mejs.afrikaans":"Afrikaans","mejs.albanian":"Albanian","mejs.arabic":"Arabic","mejs.belarusian":"Belarusian","mejs.bulgarian":"Bulgarian","mejs.catalan":"Catalan","mejs.chinese":"Chinese","mejs.chinese-simplified":"Chinese (Simplified)","mejs.chinese-traditional":"Chinese (Traditional)","mejs.croatian":"Croatian","mejs.czech":"Czech","mejs.danish":"Danish","mejs.dutch":"Dutch","mejs.english":"English","mejs.estonian":"Estonian","mejs.filipino":"Filipino","mejs.finnish":"Finnish","mejs.french":"French","mejs.galician":"Galician","mejs.german":"German","mejs.greek":"Greek","mejs.haitian-creole":"Haitian Creole","mejs.hebrew":"Hebrew","mejs.hindi":"Hindi","mejs.hungarian":"Hungarian","mejs.icelandic":"Icelandic","mejs.indonesian":"Indonesian","mejs.irish":"Irish","mejs.italian":"Italian","mejs.japanese":"Japanese","mejs.korean":"Korean","mejs.latvian":"Latvian","mejs.lithuanian":"Lithuanian","mejs.macedonian":"Macedonian","mejs.malay":"Malay","mejs.maltese":"Maltese","mejs.norwegian":"Norwegian","mejs.persian":"Persian","mejs.polish":"Polish","mejs.portuguese":"Portuguese","mejs.romanian":"Romanian","mejs.russian":"Russian","mejs.serbian":"Serbian","mejs.slovak":"Slovak","mejs.slovenian":"Slovenian","mejs.spanish":"Spanish","mejs.swahili":"Swahili","mejs.swedish":"Swedish","mejs.tagalog":"Tagalog","mejs.thai":"Thai","mejs.turkish":"Turkish","mejs.ukrainian":"Ukrainian","mejs.vietnamese":"Vietnamese","mejs.welsh":"Welsh","mejs.yiddish":"Yiddish"}};
# </script>
# <script src='https://www.ncertbooks.guru/wp-includes/js/mediaelement/mediaelement-and-player.min.js?ver=4.2.16' id='mediaelement-core-js'></script>
# <script src='https://www.ncertbooks.guru/wp-includes/js/mediaelement/mediaelement-migrate.min.js?ver=5.8.2' id='mediaelement-migrate-js'></script>
# <script id='mediaelement-js-extra'>
# var _wpmejsSettings = {"pluginPath":"\/wp-includes\/js\/mediaelement\/","classPrefix":"mejs-","stretching":"responsive"};
# </script>
# <script src='https://www.ncertbooks.guru/wp-includes/js/mediaelement/wp-mediaelement.min.js?ver=5.8.2' id='wp-mediaelement-js'></script>
# <script src='https://www.ncertbooks.guru/wp-includes/js/mediaelement/renderers/vimeo.min.js?ver=4.2.16' id='mediaelement-vimeo-js'></script>
# <script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=default&#038;ver=1.3.11' id='mathjax-js'></script>

# </body>
# </html>

# <!-- Cache served by breeze CACHE - Last modified: Fri, 10 Dec 2021 02:30:21 GMT -->


#  """
