import asyncio
from www import orm


async def test(loop):
    await orm.create_pool(loop=loop, host='127.0.0.1', user='root', password='password', db='test')

# u = User(name='Test', email='test@example.com', passwd='123456', image='about:blank')
#
# await u.save()
# await orm.destory_pool()
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()