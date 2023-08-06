<template>
  <div class="score-container">
    <div class="table-container">
      <el-table
        :data="tableData"
        :header-cell-style="{ color: '#828282',backgroundColor:'#F8F8F8'}"
        :cell-style="{color:'#5A5A5A'}"
        max-height="800"
      >
        <el-table-column
            width="52px"
        >
        </el-table-column>
        <el-table-column
            prop="name"
            label="Name"
        >
        </el-table-column>
        <el-table-column
            width="150"
        >
        </el-table-column>
        <el-table-column
            prop="target"
            label="Target Score"
            width="150"
            align="center"
        >
          <template slot-scope="scope">
           {{scope.row.target}}%
          </template>
        </el-table-column>
        <el-table-column
            prop="actual"
            label="Actual Score"
            width="150"
            align="center"
        >
          <template slot-scope="scope">
            <el-tag style="width: 120px" :type="getScoreType(scope.row.target,scope.row.actual)">
              {{scope.row.actual}}%
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column
            prop="points"
            label="Total Points"
            width="150"
            align="center"
        >
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      tableData: [
        {"name":"Lauren Vickers",
          "target":90,
          "actual":95,
          "points":69
        }, {"name":"Shazia Darby",
          "target":80,
          "actual":88,
          "points":26
        }, {"name":"Zara Cain",
          "target":85,
          "actual":81,
          "points":124
        }, {"name":"Clair Newton",
          "target":80,
          "actual":22,
          "points":82
        }, {"name":"April Bruce Kieran",
          "target":90,
          "actual":92,
          "points":26
        }
      ]
    }
  },
  methods: {
    getScoreType(target, actual) {
      if (target >= actual) {
        return 'success'
      }
      return 'danger'
    }
  }
}
</script>

<style scoped>
.score-container {
  width: 100vw;
  height: 100vh;
}
.table-container {
  padding: 50px 20px;
}
::v-deep  .el-table__row {
  cursor: pointer;
}
::v-deep .el-tag--danger {
  background-color: #ED5E61 !important;
  color: #FFF !important;
  font-size: 14px;
  font-weight: 700;
  text-align: center;
}
::v-deep .el-tag--success {
  background-color: #59B77A !important;
  color: #FFF !important;
  font-size: 14px;
  font-weight: 700;
  text-align: center;
}


</style>