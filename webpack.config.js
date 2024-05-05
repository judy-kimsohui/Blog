module.exports = {
  // 다른 설정들...
  module: {
    rules: [
      {
        test: /\.(png|jpe?g|gif)$/i,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[ext]',
              outputPath: 'images/', // 이미지가 번들에 포함될 경로
            },
          },
        ],
      },
    ],
  },
};
