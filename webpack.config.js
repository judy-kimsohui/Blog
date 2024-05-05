module: {
  rules: [
    {
      // babel loader
    },
    {
      test: /\.(png|jpg|gif|svg)$/, // 확장자가 png, jpg, gif, svg인것에 대해서만 등록
      loader: 'file-loader',
    },  
  ],
},