module.exports = {
    outputDir: "../dist",

    // relative to outputDir
    assetsDir: "static"

    // Isso aqui serve para fazer o proxy das rotas
    //todas as rotas que tiverem /api é direcionado para target
    // devServer: {
    //     proxy: {
    //       '/login': {
    //         target: 'http://179.181.94.188:5000',
    //         changeOrigin: true
    //       }
    //     }
    // }
};