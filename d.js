const Discord = require('discord.js');
const { notfound } = require('./messages');
const io = require('io');
const plt = require('matplotlib.pyplot');
const CoinGeckoAPI = require('pycoingecko').CoinGeckoAPI;

class Crypto {
  constructor(bot) {
    this.bot = bot;
    this.cg = new CoinGeckoAPI();
  }

  async crypto(ctx, coin) {
    try {
      // Get coin data
      coin = coin.toLowerCase();
      const coinData = this.cg.getCoinsMarkets('usd', coin);

      const coinSymbol = coinData[0]['symbol'].toUpperCase();
      const coinImage = coinData[0]['image'];

      const coinMarketCap = '{:,}$'.format(coinData[0]['market_cap']);
      const coinCurrentPrice = '{:,}$'.format(coinData[0]['current_price']);
      const coinPriceChangePercentage = '{:,}%'.format(coinData[0]['price_change_percentage_24h']);
      const coinTotalVolume = '{:,}$'.format(coinData[0]['total_volume']);
      const coinHigh24h = '{:,}$'.format(coinData[0]['high_24h']);
      const coinLow24h = '{:,}$'.format(coinData[0]['low_24h']);

      // Get historical price data
      const coinHistoricalData = this.cg.getCoinMarketChartByID(coin, 'usd', 7);

      const coinPrices = [];
      for (const price of coinHistoricalData['prices']) {
        coinPrices.append(price[1]);
      }

      // Create a line chart
      const fig, ax = plt.subplots();
      ax.plot(coinPrices);
      ax.setAxisOff(); // hide the axis
      // set background color of chart to black
      fig.patch.setFaceColor('#36393F');

      // Save the chart as an image file
      const buffer = io.BytesIO();
      fig.savefig(buffer, format='png', bbox_inches='tight',
                        pad_inches=0,
                        facecolor=fig.get_facecolor()
                        );
      buffer.seek(0);

      // Create a Discord message with the chart as an attachment
      const file = new Discord.MessageAttachment(buffer, 'chart.png');

      const embed = new Discord.MessageEmbed()
        .setTitle(coinSymbol)
        .setColor('#2F3136')
        .setAuthor(this.bot.user.display_name, this.bot.user.display_avatar)
        .addField('Current Price💸', coinCurrentPrice, true)
        .addField('Market Cap💰', coinMarketCap, true)
        .addField('24h-High ⬆️', coinHigh24h, true)
        .addField('24h-low ⬇️', coinLow24h, true)
        .addField('Total Volume📈', coinTotalVolume, true)
        .addField('Price Change 24h⏰', coinPriceChangePercentage, true)
        .setThumbnail(coinImage)
        .setImage('attachment://chart.png');

      await ctx.send({ embeds: [embed], files: [file] });

    } catch (error) {
      await ctx.reply(notfound(coin));
    }
  }
}

module.exports = Crypto;
