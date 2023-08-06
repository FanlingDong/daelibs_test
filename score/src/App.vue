<template>
  <div id="app">
    <score-table />
  </div>
</template>

<script>
import ScoreTable from "@/components/ScoreTable.vue";
export default {
  name: 'App',
  components: {
    ScoreTable
  }
}
</script>

<style>
body {
  margin: 0;
  padding: 0;
}

::-webkit-scrollbar {width:8px; height:6px; background-color:transparent;} /*定义滚动条高宽及背景 高宽分别对应横竖滚动条的尺寸*/
::-webkit-scrollbar-track {background-color: rgba(117,116,116,0.3);  } /*定义滚动条轨道 内阴影+圆角*/
::-webkit-scrollbar-thumb {background-color:rgba(0,0,0,0.3); border-radius:6px;} /*定义滑块 内阴影+圆角*/
::-webkit-scrollbar{display: none}
::-webkit-scrollbar{display: block}


</style>
