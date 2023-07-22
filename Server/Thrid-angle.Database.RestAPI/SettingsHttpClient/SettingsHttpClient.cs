using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Http;

namespace Thrid_angle.Database.RestAPI.SettingsHttpClient
{
    internal class SettingsHttpClient
    {

        private static HttpClient sharedClient = new()
        {
            BaseAddress = new Uri("https://jsonplaceholder.typicode.com"),
        };





    }
}
