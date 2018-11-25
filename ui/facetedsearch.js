!function(){var n,e={items:[{a:2,b:1,c:2},{a:2,b:2,c:1},{a:1,b:1,c:1},{a:3,b:3,c:1}],facets:{a:"Title A",b:"Title B",c:"Title C"},resultSelector:"#results",facetSelector:"#facets",facetContainer:"<div class=facetsearch id=<%= id %> ><br></div>",facetTitleTemplate:'<button class="facettitle fbtn btn btn-light" id=<%= title %> ><%= title %></button>',facetListContainer:"<div class=facetlist></div>",listItemTemplate:'<div class="facetitem" id="<%= id %>"><%= name %> <span class=facetitemcount>(<%= count %>)</span><br></div>',bottomContainer:"<br><div class=bottomline></div>",orderByTemplate:'<br><div class=orderby><span class="orderby-title"><br>Sort by: </span><br><ul style="display:inline-block"><br><% _.each(options, function(value, key) { %><button class="btn sbtn btn-light orderbyitem" id=orderby_<%= key %>><%= value %> </button> <br><% }); %></ul></div>',countTemplate:"<br><div class=facettotalcount><%= count %> Results</div><br>",deselectTemplate:'<br><button class="deselectstartover btn btn-primary">Deselect all filters</button>',resultTemplate:"<div class=facetresultbox><%= name %></div>",noResults:"<div class=results>Sorry, but no items match these criteria</div>",orderByOptions:{a:"by A",b:"by B",RANDOM:"by random"},state:{orderBy:!1,filters:{}},showMoreTemplate:'<div id=showmore class="col-sm-offset-6"><a id=showmorebutton>Show more</a></div>',enablePagination:!0,paginationCount:20},l={};function s(){l.currentResults=_.select(l.items,function(a){var c=!0;return _.each(l.state.filters,function(t,e){$.isArray(a[e])?0==_.intersect(a[e],t).length&&(c=!1):t.length&&-1==_.indexOf(t,a[e])&&(c=!1)}),c}),_.each(l.facetStore,function(t,a){_.each(t,function(t,e){l.facetStore[a][e].count=0})}),_.each(l.facets,function(t,e){_.each(l.currentResults,function(t){$.isArray(t[e])?_.each(t[e],function(t){l.facetStore[e][t].count+=1}):void 0!==t[e]&&(l.facetStore[e][t[e]].count+=1)})}),_.each(l.state.filters,function(t,e){_.each(l.facetStore[e],function(t){0==t.count&&l.state.filters[e].length&&(t.count="+")})}),l.state.shownResults=0}function u(){l.state.orderBy&&($(".activeorderby").removeClass("activeorderby"),$("#orderby_"+l.state.orderBy).addClass("activeorderby"),l.currentResults=_.sortBy(l.currentResults,function(t){return"RANDOM"==l.state.orderBy?1e4*Math.random():t[l.state.orderBy]}))}function f(){var s=_.template(l.listItemTemplate);_.each(l.facetStore,function(t,n){_.each(t,function(t,e){var a={id:t.id,name:e,count:t.count},c=$(s(a)).html();$("#"+t.id).html(c),l.state.filters[n]&&0<_.indexOf(l.state.filters[n],e)?(console.log(a.count),$("#"+t.id).addClass("activefacet")):$("#"+t.id).removeClass("activefacet")})}),countHtml=_.template(l.countTemplate,{count:l.currentResults.length}),$(l.facetSelector+" .facettotalcount").replaceWith(countHtml)}function d(){$(l.resultSelector).html(0==l.currentResults.length?l.noResults:""),r()}function r(){for(var t=l.enablePagination?Math.min(l.currentResults.length-l.state.shownResults,l.paginationCount):l.currentResults.length,e="",a=_.template(l.resultTemplate),c=l.state.shownResults;c<l.state.shownResults+t;c++)e=e+a($.extend(l.currentResults[c],{totalItemNr:c,batchItemNr:c-l.state.shownResults,batchItemCount:t}));$(l.resultSelector).append(e),n||(n=$(l.showMoreTemplate).click(r),$(l.resultSelector).after(n)),0==l.state.shownResults&&n.show(),l.state.shownResults+=t,l.state.shownResults==l.currentResults.length&&$(n).hide(),$(l.resultSelector).trigger("facetedsearchresultupdate")}jQuery.facetelize=function(t){$.extend(l,e,t),l.currentResults=[],l.facetStore={},$(l.facetSelector).data("settings",l),_.each(l.facets,function(t,e){l.facetStore[e]={}}),_.each(l.items,function(a){_.each(l.facets,function(t,e){$.isArray(a[e])?_.each(a[e],function(t){l.facetStore[e][t]=l.facetStore[e][t]||{count:0,id:_.uniqueId("facet_")}}):void 0!==a[e]&&(l.facetStore[e][a[e]]=l.facetStore[e][a[e]]||{count:0,id:_.uniqueId("facet_")})})}),_.each(l.facetStore,function(t,e){var a=_.keys(l.facetStore[e]).sort();l.facetSortOption&&l.facetSortOption[e]&&(a=_.union(l.facetSortOption[e],a));var c={};_.each(a,function(t){c[t]=l.facetStore[e][t]}),l.facetStore[e]=c}),s(),u(),function(){var r=_.template(l.listItemTemplate),o=_.template(l.facetTitleTemplate),i=_.template(l.facetContainer);$(l.facetSelector).html(""),_.each(l.facets,function(t,n){var e=$(i({id:n})),a={title:t},c=$(o(a));e.append(c);var s=$(l.facetListContainer);_.each(l.facetStore[n],function(t,e){var a={id:t.id,name:e,count:t.count},c=$(r(a));0<_.indexOf(l.state.filters[n],e)&&0<a.count&&c.addClass("activefacet"),s.append(c)}),e.append(s),$(l.facetSelector).append(e)}),$(".facetitem").click(function(t){var c,n,e=(c=this.id,n=!1,_.each(l.facetStore,function(t,a){_.each(t,function(t,e){t.id==c&&(n={facetname:a,filtername:e})})}),n);!function(t,e){l.state.filters[t]=l.state.filters[t]||[],-1==_.indexOf(l.state.filters[t],e)?l.state.filters[t].push(e):(l.state.filters[t]=_.without(l.state.filters[t],e),0==l.state.filters[t].length&&delete l.state.filters[t]);s()}(e.facetname,e.filtername),$(l.facetSelector).trigger("facetedsearchfacetclick",e),u(),f(),d()});var t=$(l.bottomContainer);countHtml=_.template(l.countTemplate,{count:l.currentResults.length}),$(t).append(countHtml);var e=_.template(l.orderByTemplate),a=$(e({options:l.orderByOptions}));$(t).append(a),$(l.facetSelector).append(t),$(".orderbyitem").each(function(){var t=this.id.substr(8);l.state.orderBy==t&&$(this).addClass("activeorderby")}),$(".orderbyitem").click(function(t){var e=this.id.substr(8);l.state.orderBy=e,$(l.facetSelector).trigger("facetedsearchorderby",e),l.state.shownResults=0,u(),d()});var c=$(l.deselectTemplate).click(function(t){l.state.filters={},jQuery.facetUpdate()});$(t).append(c),$(l.facetSelector).trigger("facetuicreated")}(),d()},jQuery.facetUpdate=function(){s(),u(),f(),d()}}();