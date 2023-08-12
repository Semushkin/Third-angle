using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Thrid_angle.Database.RestAPI.Mehtods
{
    public interface IHelperMethodsDatabase
    {
         public (Guid IdOrderCard, int NumberCard) BasketNewGuidOrderCard(Guid IdUser, bool NewNumberOrderCard);
    }
}
